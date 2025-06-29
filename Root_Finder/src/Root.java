public class Root {
	public static Double calculate(Function f, double a, double b, int n, double alpha) {
		double ya = f.run(a);
		double yb = f.run(b);
		double x = (a + b) / 2;
		double yx = f.run(x);
		for (int i = 1; i <= n; i = i + 1) {
			x = (a + b) / 2;
			yx = f.run(x);
			if (Math.signum(ya) != Math.signum(yx)) {
				b = x;
				yb = yx;
			}
			else if (Math.signum(yx) != Math.signum(yb)) {
				a = x;
				ya = yx;
			}
			else {
				if (Math.abs(f.run((a + x) / 2)) <= Math.abs(f.run((x + b) / 2))) {
					b = x;
					yb = yx;
				}
				else {
					a = x;
					ya = yx;
				}
			}
		}
		if (Math.abs(yx) < alpha) {
			return x;
		}
		else if (Math.abs(ya) < alpha) {
			return a;
		}
		else if (Math.abs(yb) < alpha) {
			return b;
		}
		else {
			return null;
		}
	}
	public static Double calculate(Function f, double a, double b) {
		return calculate(f, a, b, 100, 0.000001);
	}
}