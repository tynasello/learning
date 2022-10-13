interface Subject {
    fun registerObserver(observer: Observer)
    fun notifyObservers(notification: String)
}