import streamlit as st

def main():
    # Apply the gradient background with lighter pink and rose shades
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(45deg, #f8c8d4, #ffb3d9, #ffccf5);  /* Light Pink, Soft Rose gradient */
            color: black;  /* Change text color to black for better contrast */
            background-size: 100% 100%;  /* Ensure the gradient covers the full background */
            height: 100vh;  /* Ensure it takes up the entire viewport height */
            margin: 0;
        }
        .stApp {
            background-color: transparent;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.title('Simple Calculator')
    st.write('Enter Two Numbers of Your Choice')

    col, col2 = st.columns(2)
    num1 = col.number_input('Enter Your First Number')
    num2 = col2.number_input('Enter Your Second Number')

    operation = st.selectbox('Select Your Operation', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

    if st.button('Calculate'):
        result = None
        
        # Check for division by zero first
        if operation == 'Division':
            if num2 == 0:
                st.error('Cannot Divide By Zero')
            else:
                result = num1 / num2
                st.write('The Quotient is:', num1 // num2)
                st.write('The Remainder is:', num1 % num2)
                st.write('The Absolute Difference is:', abs(num1 - num2))
                st.write('The Square Root of First Number is:', num1 ** 0.5)
                st.write('The Cube Root of First Number is:', num1 ** (1/3))
        
        # Perform other operations
        elif operation == 'Addition':
            result = num1 + num2
        elif operation == 'Subtraction':
            result = num1 - num2
        elif operation == 'Multiplication':
            result = num1 * num2
        
        if result is not None:
            st.success(f'Result: {result}')

            st.write('Build With ❤ By Shan E Zehra')

if __name__ == '__main__':
    main()
