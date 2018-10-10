class X
{
private:
    int i;
    int *pi;
public:
    X()
        : pi(new int)
    { }
    X(const X& copy)   // <-- copy ctor
        : i(copy.i), pi(copy.pi)
    { }
};
