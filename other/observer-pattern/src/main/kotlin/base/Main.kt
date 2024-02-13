package base

import Desktop
import NotificationManager
import Phone
import java.text.SimpleDateFormat
import java.util.*

fun main(args: Array<String>) {

    val sdf = SimpleDateFormat("dd/M/yyyy hh:mm:ss")

    val notificationManager = NotificationManager()
    val phone = Phone(notificationManager)
    val desktop = Desktop(notificationManager)

    notificationManager.notifyObservers("Notification from notification manager ${sdf.format(Date())}")
}
