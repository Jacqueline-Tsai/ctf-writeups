from sage.all import *
import itertools
import sys

# https://github.com/elliptic-shiho/crypto_misc/blob/master/small_root/coron.sage
# references: https://github.com/mimoo/RSA-and-LLL-attacks/blob/master/boneh_durfee.sage
def matrix_overview(BB):
  for ii in range(BB.dimensions()[0]):
    a = ('%02d ' % ii)
    for jj in range(BB.dimensions()[1]):
      a += ' ' if BB[ii,jj] == 0 else 'X'
      if BB.dimensions()[0] < 60:
        a += ' '
    print(a)


def coron_bivariate_integer_small_root(poly, XX, YY, kk):
  '''
  Solve Bivariate Polynomial Small Root
  Implementation of [1].
  References:
    * [1] Jean-Se'bastien Coron. 2004. "Finding Small Roots of Bivariate Integer Polynomial Equations Revisited"
'''

  p00 = poly.constant_coefficient()
  assert gcd(p00, XX * YY) == 1, 'p00 and XY has common divisor'
  x, y = poly.parent().gens()

  monomials = list(poly.monomials())
  monomials.sort()

  WW = max(map(lambda t: abs(poly.monomial_coefficient(t)) * t(XX, YY), monomials))
  uu = WW + 1 + ZZ((1 - WW) % abs(p00))
  delta = max(poly.degree(x), poly.degree(y))
  omega = (delta + kk + 1)^2
  nn = uu * (XX * YY)^kk

  print('[+] Bound Check...')
  sys.stdout.flush()
  if RR(XX*YY) < RR(WW^((2/3) * delta)):
    print('OK')
  else:
    print('Failed (maybe not found solution...)')

  if p00 != 0:
    F = Zmod(nn)
    PF = PolynomialRing(F, 'xn, yn')
    q = poly.parent()(PF(poly) * F(p00)^-1)

  # Construct Polynomial for lattice construction (cf. [1] p.7)
  qij = {}
  for i in range(0, kk + 1):
    for j in range(0, kk + 1):
      qij[i, j] = x^i * y^j * XX^(kk-i) * YY^(kk-j) * q
  index_range = sorted(list(set(itertools.product(range(0, delta + kk + 1), repeat=2)) - set(itertools.product(range(0, kk + 1), repeat=2))))
  for i, j in index_range:
    qij[i, j] = x^i * y^j * nn

  monomials = set()
  for k in qij.keys():
    monomials |= set(qij[k].monomials())
  monomials = list(monomials)
  monomials.sort()

  M = Matrix(ZZ, omega, omega)
  assert len(monomials) == omega

  # Construct Lattice
  col = 0
  for i in range(kk + 1):
    for j in range(kk + 1):
      q_cur = qij[i, j]
      for ii, m in enumerate(monomials):
        M[col, ii] = q_cur.monomial_coefficient(m) * m(XX, YY)
      col += 1

  for i, j in index_range:
    q_cur = qij[i, j]
    for ii, m in enumerate(monomials):
      M[col, ii] = q_cur.monomial_coefficient(m) * m(XX, YY)
    col += 1

  matrix_overview(M)

  print('\n===\n')

  # LLL
  B = M.LLL()

  matrix_overview(B)

  # Solve equatation for each variable
  PK = PolynomialRing(ZZ, 'xk, yk')
  xk, yk = PK.gens()

  PX = PolynomialRing(ZZ, 'xs')
  xs = PX.gen()
  PY = PolynomialRing(ZZ, 'ys')
  ys = PY.gen()

  monomials = map(lambda t: PK(t), monomials)
  pkf = PK(poly)
  x_root = y_root = None

  # Re-construct polynomial from LLL-reduced matrix `B`
  H = [(i, 0) for i in range(omega)]
  H = dict(H)
  tmp = list(monomials)
  for i in range(omega):
    for j in range(omega):
      H[i] += PK((tmp[j] * B[i, j]) / tmp[j](XX, YY))

  # Solve for `x`
  # My Heuristics: finding resultant from all polynomials
  for i in range(omega):
    pol = H[i].resultant(pkf, yk).subs(xk=xs)
    if not isinstance(pol, Integer):
      roots = pol.roots()
      roots = filter(lambda t: 0 < t[0] < XX, roots)
      list_root = list(roots)
      if len(list_root) != 0:
        print('[+] Found Solution for x')
        x_root = list_root[0][0]
        break
  else:
    print('[+] solution not found...')
    return None, None

  # Solve for `y`
  roots_y = PY(pkf.subs(xk=x_root).subs(yk=ys)).roots()
  roots_y = filter(lambda t: 0 < t[0] < YY, roots_y)
  list_roots_y = list(roots_y)
  if len(list_roots_y) != 0:
    print('[+] Found Solution for y')
    y_root = list_roots_y[0][0]
  return x_root, y_root


def main():
  n = 9339907490332757184081791088025727272232111017821633821627096690050603017465600111366599281730392481551285009110375533939227876305083592970674713852269426685640639133973376965604743259731930968981662180703656576345020102532031593703717582301521132732090950792215247318912019816440274078455093165801529719426102806667505183892504732885710674933075464485910216519152114283949873630762674149267888293544936494890601836747237466065845148550230344936539099066551621221057576916542155924614345400753868112562999697987501455532686267016587509789833458851970531593859049825764883084892049313380197483575337147580165595526543
  p0 = 95945380781649189259833894885346136807219971089273188374854152478373734459923151575966980869144655181902212692891070962472503313499006444446833276451458038927074771901508711118229884844865130895102052862269584357080803347892801635289960266409563421282012361679896091787691523957878352989783585065142228877312
  q0 = ((n >> 512) // (p0 >> 256)) << 256

  XX = next_prime(2^256)
  YY = next_prime(2^256)
  kk = 1

  PR = PolynomialRing(ZZ, 'x, y')
  x, y = PR.gens()

  f = (p0 * q0 - n) + q0 * x + p0 * y + x*y
  roots = coron_bivariate_integer_small_root(f, XX, YY, kk)
  assert f(roots[0], roots[1]) == 0
  p = p0+roots[0]
  q = q0+roots[1]
  assert p*q == n
  print(p,q)

if __name__ == '__main__':
  main()