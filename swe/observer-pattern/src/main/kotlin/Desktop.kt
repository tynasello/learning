class Desktop(notificationManager: NotificationManager) : Observer {

    init {
        notificationManager.registerObserver(this)
    }

    override fun update(notification: String) {
        println("-- Desktop receiving notification -- $notification")
    }
}