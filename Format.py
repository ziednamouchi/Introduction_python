#FORMAT
# Conversion types
# %s string
# %d decimal integer
# %x hex integer
# %o octal integer
# %f decimal float
# %e exponential float
# %g decimal or exponential float
# %% a literal %
#examples with interger
print('%s' % 42)#string
print('%x' % 42)#hex int
print('%o' % 42)#octal int
#examples with float
print('%s' % 7.03)#string
print('%f' % 7.03)#decimal float
print('%e' % 7.03)#exponential float
print('%g' % 7.03)#decimal or exponential float
#An integer and a literal %
print('%d%%' % 100)
#Some string and integer interpolation
actor = 'Richard Gere'
cat = 'chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))
n = 42
f = 7.03
s = 'string cheese'
#default widths
print('%d %f %s' % (n, f, s))
#minimum field width of 10 characters for each variable
print('%10d %10f %10s' % (n, f, s))
#same field width, but align to the left
print('%-10d %-10f %-10s' % (n, f, s))
#New style formatting with {} and format
print('{} {} {}'.format(n, f, s))
#With new-style, you can specify the order
print('{2} {0} {1}'.format(f, s, n))
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))
#combining our three values into a dictionary
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))
#The final option is the fill character
print('{0:!^20s}'.format('BIG SALE'))
print('{0:?^20s}'.format('BIG SALE'))
