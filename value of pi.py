#alogorthim used for it

import mpmath
import os

def compute_pi(num_digits):
    """
    Compute the digits of pi to the specified number of digits using mpmath library.
    
    Parameters:
    num_digits : int
        Number of digits of pi to compute.
    
    Returns:
    str
        String representation of pi with the specified number of digits.
    """
    # Set the precision to the desired number of digits
    mpmath.mp.dps = num_digits + 1  # +1 to account for the leading '3'

    # Compute pi using mpmath's pi function
    pi_value = mpmath.mp.pi

    # Convert pi to a string with the specified number of digits
    pi_string = str(pi_value)

    return pi_string

def save_pi_digits(pi_string, num_digits):
    """
    Save the computed digits of pi to a text file.
    
    Parameters:
    pi_string : str
        String representation of pi with the specified number of digits.
    num_digits : int
        Number of digits of pi computed and stored.
    """
    # Get the directory path of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Specify the output file path (in the same directory as the script)
    output_file = os.path.join(script_dir, f"pi_{num_digits}_digits.txt")

    # Write the pi string to the output file
    with open(output_file, "w") as file:
        file.write(pi_string)

    print(f"{num_digits} digits of pi have been saved to '{output_file}'.")

if __name__ == "__main__":
    # Specify the desired number of digits of pi
    num_digits = 10000001  # Change this to the desired number of digits

    # Compute pi to the specified number of digits
    pi_string = compute_pi(num_digits)

    # Save the computed digits of pi to a text file in the same directory as the script
    save_pi_digits(pi_string, num_digits)
