package standard;

public abstract class Pizza {
    protected String description;
    protected double cost;

    public String getDescription() {
        return this.description;
    }

    public double getCost() {
        return this.cost;
    }

    // the problem with this approach is that it does not adhere to the open close
    // principle in SOLID
    public void addTopping(String name) {
        if (name == "basil") {
            this.cost += .25;
            this.description += ", basil";
        } else if (name == "tomato") {
            this.description += ", tomato";
            this.cost += .45;
        } else if (name == "mozzarella") {
            this.description += ", mozzarella";
            this.cost += .55;
        }
    }

}
