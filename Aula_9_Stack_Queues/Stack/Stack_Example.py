import Aula_9_Stack_Queues.Stack.Stack_Class as stk

st = stk.Stack()

st.push(1)
st.push(2)
st.push(3)

print(str(len(st)))

value = st.top()

print("Último da pilha: " + str(value))

value = st.pop()

print("Ultimo elemento da pilha: "+ str(value))


print("Estado da pilha (empty ?): " + str(st.is_empty()))

st.pop()
st.pop()

print("Estado da pilha (empty ?): " + str(st.is_empty()))
