function NotificationModal({ notification, onClose }) {
  if (!notification) {
    return null;
  }

  return (
    <div className="modal-overlay notification-overlay">
      <div className={`modal notification-modal ${notification.type}`}>
        <button className="close-button" onClick={onClose} aria-label="Close">
          x
        </button>
        <div className="notification-icon">
          {notification.type === "error" ? "!" : "✓"}
        </div>
        <h2>{notification.title}</h2>
        <p>{notification.message}</p>
        <button className="auth-submit-button" onClick={onClose}>
          Continue
        </button>
      </div>
    </div>
  );
}

export default NotificationModal;