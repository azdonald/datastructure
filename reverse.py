from stack import Stack
def rs(string):
    st = Stack()
    ns = []
    for ch in string:
        st.push(ch)
    while not st.isEmpty():
        ns.append(st.pop())
        

    newstring = ''.join(ns)
    print newstring


if __name__ == "__main__":
    rs('i am a boy')
