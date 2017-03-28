#tuples they are similar to lists and strings
#1)Tuples are immutable i.e cant be altered
#2)sort,reverse,append functions are not possible with tuples as they are all alteration functions but tuple is immutable so not possible
#3)Tuples are used when we want to create temporary list, i.e when we are not going to change the values but only using them
#4)tuples can be accessed fast when compared to lists

tup1=(3,1,2,5,4);
print type(tup1);
for i in tup1:
    print i;
#altering not possible
#tup1[0]=10

tup2=('akarsh',1,2)
print tup2

#tuples on lhs and rhs sides
(akarsh,harun)=(507,'504')
print akarsh,harun
#or
arun,vp=1,2
print arun,vp

#tuples are comparable similar to lists
print (1,2)<(2,3)#checks the first vals if condition staisfied it doesnt check for next vals if not it checks for next vals
print ('arun','harun')<('akarsh','vp')

dic={"a":1,"z":2,"c":3}
#sorting dictionary is not possible directly
t=dic.items();#converted to list of tuples
print t;
t.sort();
print "after sorting list of tuples: ",t

#   or in one line
print sorted([(k,v) for k,v in dic.items()]) 