# Bitwise operators

def bitwise_ops(n1, n2, num):
    step1 = n1 & n2 # and

    step2 = n1 | n2 # or

    step3 = n1 ^ n2 # xor

    step4 = ~step1 # not

    step5 = step2 << num # left shift

    step6 = step3 >> num # right shift

    final_result = step4 & (step5 | step6)

    print(f"\n Intermediate results: \n")
    print(f"    Not = {step4}")
    print(f"\n    Left shift({step2} << {num}) = {step5}")
    print(f"\n    Right Shift({step3} >> {num}) = {step6}")
    print(f"\n    Final result({step4} & ({step5} | {step6})) =  {final_result}")

try:
    num1 = int(input("\n enter number 1: "))
    num2 = int(input("\n enter number 2: "))

    shift = int(input("\n Enter the bits to shift: "))

    bitwise_ops(num1, num2, shift)

except ValueError as e:
    print(f"Invalid input: {e}")