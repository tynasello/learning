package decorator_pattern;

public abstract class Pizza {
    public String description;

    public String getDescription() {
        return description;
    }

    public abstract double cost();
}
