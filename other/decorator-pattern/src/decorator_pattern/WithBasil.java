package decorator_pattern;

public class WithBasil extends PizzaDecorator {
    Pizza pizza;
    double basilCost = .25;

    public WithBasil(Pizza pizza) {
        this.pizza = pizza;
        this.description = pizza.description + ", basil";

    }

    @Override
    public double cost() {
        return pizza.cost() + basilCost;
    }
}
