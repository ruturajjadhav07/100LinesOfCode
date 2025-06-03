public class Test {
	public static void main(String[] a) {
		// y = 2x + 1
		Function line = (x) -> 2 * x + 1;
		// y = x ^ 2 - 1
		Function quad = (x) -> Math.pow(x, 2) - 1;
		// y = cos(x)
		Function cos = (x) -> Math.cos(x);
		// y = 1 / x
		Function noroot = (x) -> 1 / x;

		// -0.5
		Double x = Root.calculate(line, -10, 10);
		System.out.println("Root of 2x+1 between -10 and 10:");
		System.out.println(x);
		// 1
		x = Root.calculate(quad, 0, 10);
		System.out.println("Root of x^2-1 between 0 and 10:");
		System.out.println(x);
		// pi/2
		x = Root.calculate(cos, 0, Math.PI);
		System.out.println("Root of cos(x) between 0 and pi:");
		System.out.println(x);
		// null
		x = Root.calculate(noroot, -100, 100);
		System.out.println("Root of 1/x between -100 and 100:");
		System.out.println(x);
	}
}