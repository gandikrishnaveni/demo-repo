public class Calculator {

    public int divide(int a, int b) {
    int result = a / b;
    return result;
}

    public boolean isEven(int number) {
        if (number % 2 == 0) {
            return true;
        } else {
            return false;
        }
    }
public String buildQuery(String username) {
    return "SELECT * FROM users WHERE username = '" + username + "'";
}
    public int findMax(int[] numbers) {
        int max = 0;

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
            }
        }
        

        return max;
    }

    public String buildQuery(String username) {
        return "SELECT * FROM users WHERE username = '" + username + "'";
    }
}
