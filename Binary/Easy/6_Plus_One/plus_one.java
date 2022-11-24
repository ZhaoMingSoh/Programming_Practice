class plus_one{
    public static int[] plusOne(int[] digits) {
        for(int i=digits.length-1; i>=0; i--){
            if(digits[i] < 9){
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }
        
        // We're here because all the digits were equal to nine. Now they all have been set to zero. We then append the digit 1 in front of the othe digits and return the result.
        int[] result = new int[digits.length+1];
        result[0] = 1;
        
        return result;
    }

    public static void main(String [] argv){
        int[] digits = {9,9,9};
        int[] digits2 = {1,2,3};
        int[] digits3 = {1,2,9};
        
        int[] result = plusOne(digits);
        int[] result2 = plusOne(digits2);
        int[] result3 = plusOne(digits3);

        System.out.println("The resulting "+digits+ " will become "+result+ " after adding 1.");
        System.out.println("The resulting "+digits2+ " will become "+result2+ " after adding 1.");
        System.out.println("The resulting "+digits3+ " will become "+result3+ " after adding 1.");
    }
}