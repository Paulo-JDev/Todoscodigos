print('|========================== Conversor de Metro ========================|')
n1 = float(input('um valor em metros:'))
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
print('{} metros em mm são {}mm\n{} metros em cm são:{:.2f}cm \n{} metros em dm são:{:.2f}dm'.format(n1, mm, n1, cm, n1, dm))
print('{} metros em hm são {}'.format(n1, dam))
print('{} metros em dam são {}'.format(n1, hm))
print('{} metros em km são {}km'.format(n1, km))
