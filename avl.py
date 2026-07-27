class N:
    def __init__(self,k):self.k,self.l,self.r,self.h=k,None,None,1
class T:
    def __init__(self):self.r=None
    def _h(self,n):return n.h if n else 0
    def _u(self,n):n.h=max(self._h(n.l),self._h(n.r))+1
    def _b(self,n):return self._h(n.l)-self._h(n.r)
    def _L(self,n):x=n.r;n.r=x.l;x.l=n;self._u(n);self._u(x);return x
    def _R(self,n):x=n.l;n.l=x.r;x.r=n;self._u(n);self._u(x);return x
    def _reb(self,n):
        self._u(n)
        if self._b(n)>1:
            if self._b(n.l)<0:n.l=self._L(n.l)
            return self._R(n)
        if self._b(n)<-1:
            if self._b(n.r)>0:n.r=self._R(n.r)
            return self._L(n)
        return n
    def insert(self,k):self.r=self._i(self.r,k)
    def _i(self,n,k):
        if not n:return N(k)
        if k<n.k:n.l=self._i(n.l,k)
        elif k>n.k:n.r=self._i(n.r,k)
        return self._reb(n)
    def search(self,k):
        n=self.r
        while n:
            if k==n.k:return True
            n=n.l if k<n.k else n.r
        return False
    def inorder(self):
        r=[];self._w(self.r,r);return r
    def _w(self,n,r):
        if n:self._w(n.l,r);r.append(n.k);self._w(n.r,r)

a=T()
for i in [10,20,30,40,50,25,70,100,90,52,120,39,190,740]:a.insert(i)
print(a.inorder())
print(a.search(30))
