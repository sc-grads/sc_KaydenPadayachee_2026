import { useEffect, useState } from "react";

import "./App.css";
import AboutSection from "./components/AboutSection";
import ContactSection from "./components/ContactSection";
import Footer from "./components/Footer";
import Hero from "./components/Hero";
import Navbar from "./components/Navbar";
import NotificationModal from "./components/NotificationModal";
import ProductsSection from "./components/ProductsSection";

const API_URL = "http://127.0.0.1:5000";

function App() {
  const [products, setProducts] = useState([]);

  const [loading, setLoading] = useState(true);

  const [showAuth, setShowAuth] = useState(false);

  const [authMode, setAuthMode] = useState("login");

  const [firstName, setFirstName] = useState("");

  const [lastName, setLastName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [confirmPassword, setConfirmPassword] = useState("");

  const [securityQuestion, setSecurityQuestion] = useState("");

  const [securityAnswer, setSecurityAnswer] = useState("");

  const [forgotStep, setForgotStep] = useState("email");

  const [forgotUserId, setForgotUserId] = useState(null);

  const [forgotQuestion, setForgotQuestion] = useState("");

  const [forgotAnswer, setForgotAnswer] = useState("");

  const [newPassword, setNewPassword] = useState("");

  const [forgotConfirmPassword, setForgotConfirmPassword] = useState("");

  const [message, setMessage] = useState("");

  const [error, setError] = useState("");

  const [token, setToken] = useState(localStorage.getItem("access_token"));

  const [user, setUser] = useState(null);

  const [showCart, setShowCart] = useState(false);

  const [cart, setCart] = useState([]);

  const [cartTotal, setCartTotal] = useState(0);

  const [cartLoading, setCartLoading] = useState(false);

  const [showOrders, setShowOrders] = useState(false);

  const [orders, setOrders] = useState([]);

  const [ordersLoading, setOrdersLoading] = useState(false);

  const [ordersError, setOrdersError] = useState("");

  const [showCheckout, setShowCheckout] = useState(false);

  const [checkoutLoading, setCheckoutLoading] = useState(false);

  const [checkoutMessage, setCheckoutMessage] = useState("");

  const [checkoutError, setCheckoutError] = useState("");

  const [shippingFirstName, setShippingFirstName] = useState("");

  const [shippingLastName, setShippingLastName] = useState("");

  const [shippingPhone, setShippingPhone] = useState("");

  const [shippingAddress, setShippingAddress] = useState("");

  const [shippingSuburb, setShippingSuburb] = useState("");

  const [shippingCity, setShippingCity] = useState("");

  const [shippingProvince, setShippingProvince] = useState("");

  const [shippingPostalCode, setShippingPostalCode] = useState("");

  const [cardHolderName, setCardHolderName] = useState("");

  const [cardNumber, setCardNumber] = useState("");

  const [cardCvv, setCardCvv] = useState("");

  const [selectedProduct, setSelectedProduct] = useState(null);

  const [showAdmin, setShowAdmin] = useState(false);

  const [productName, setProductName] = useState("");

  const [productDescription, setProductDescription] = useState("");

  const [productPrice, setProductPrice] = useState("");

  const [productCategory, setProductCategory] = useState("");

  const [productBrand, setProductBrand] = useState("");

  const [productStock, setProductStock] = useState("");

  const [productImage, setProductImage] = useState(null);

  const [adminMessage, setAdminMessage] = useState("");

  const [adminError, setAdminError] = useState("");

  const [addingProduct, setAddingProduct] = useState(false);

  const [editingProduct, setEditingProduct] = useState(null);

  const [editingImage, setEditingImage] = useState(null);

  const [updatingProduct, setUpdatingProduct] = useState(false);

  const [showProfile, setShowProfile] = useState(false);

  const [profileFirstName, setProfileFirstName] = useState("");

  const [profileLastName, setProfileLastName] = useState("");

  const [profileEmail, setProfileEmail] = useState("");

  const [profilePhone, setProfilePhone] = useState("");

  const [profileAddress, setProfileAddress] = useState("");

  const [profileSuburb, setProfileSuburb] = useState("");

  const [profileCity, setProfileCity] = useState("");

  const [profileProvince, setProfileProvince] = useState("");

  const [profilePostalCode, setProfilePostalCode] = useState("");

  const [currentPassword, setCurrentPassword] = useState("");

  const [profileNewPassword, setProfileNewPassword] = useState("");

  const [profileConfirmPassword, setProfileConfirmPassword] = useState("");

  const [passwordMessage, setPasswordMessage] = useState("");

  const [passwordError, setPasswordError] = useState("");

  const [passwordLoading, setPasswordLoading] = useState(false);

  const [profileMessage, setProfileMessage] = useState("");

  const [profileError, setProfileError] = useState("");

  const [profileLoading, setProfileLoading] = useState(false);

  const [showCustomers, setShowCustomers] = useState(false);

  const [customers, setCustomers] = useState([]);

  const [customersLoading, setCustomersLoading] = useState(false);

  const [customerMessage, setCustomerMessage] = useState("");

  const [customerError, setCustomerError] = useState("");

  const [adminOrders, setAdminOrders] = useState([]);

  const [adminOrdersLoading, setAdminOrdersLoading] = useState(false);

  const [adminOrdersError, setAdminOrdersError] = useState("");

  const [notification, setNotification] = useState(null);

  const [searchTerm, setSearchTerm] = useState("");

  const [selectedCategory, setSelectedCategory] = useState("All");

  const [selectedBrand, setSelectedBrand] = useState("All");

  const [sortOption, setSortOption] = useState("default");

  const showNotification = (title, message, type = "success") => {
    setNotification({ title, message, type });
  };

  const readResponse = async (response) => {
    const data = await response.json();
    return data;
  };

  const loadProducts = async () => {
    try {
      setLoading(true);

      const response = await fetch(`${API_URL}/products`);

      if (!response.ok) {
        throw new Error("Failed to load products.");
      }

      const data = await response.json();

      setProducts(data);
    } catch (err) {
      console.error(err);

      setError("Could not load products.");
    } finally {
      setLoading(false);
    }
  };

  const loadProfile = async () => {
    if (!token) {
      setUser(null);

      return;
    }

    try {
      const response = await fetch(`${API_URL}/profile`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();

        setUser(data);
      } else {
        localStorage.removeItem("access_token");

        setToken(null);

        setUser(null);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const loadCart = async () => {
    if (!token) {
      setCart([]);

      setCartTotal(0);

      return;
    }

    try {
      setCartLoading(true);

      const response = await fetch(`${API_URL}/cart`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        throw new Error("Failed to load cart.");
      }

      const data = await response.json();

      setCart(data.items || []);

      setCartTotal(data.total || 0);
    } catch (err) {
      console.error(err);
    } finally {
      setCartLoading(false);
    }
  };

  const loadOrders = async () => {
    if (!token || user?.role !== "customer") {
      return;
    }

    setOrdersLoading(true);
    setOrdersError("");

    try {
      const response = await fetch(`${API_URL}/orders`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (!response.ok) {
        setOrdersError(data.message || "Failed to load orders.");
        return;
      }

      setOrders(data || []);
    } catch (err) {
      console.error(err);
      setOrdersError("Could not connect to the server.");
    } finally {
      setOrdersLoading(false);
    }
  };

  const openProfile = async () => {
    if (!token || user?.role !== "customer") {
      return;
    }

    setProfileMessage("");
    setProfileError("");
    setShowProfile(true);

    try {
      const response = await fetch(`${API_URL}/profile`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (!response.ok) {
        setProfileError(data.message || "Failed to load profile.");
        return;
      }

      setProfileFirstName(data.first_name);
      setProfileLastName(data.last_name);
      setProfileEmail(data.email);
      setProfilePhone(data.phone || "");
      setProfileAddress(data.address || "");
      setProfileSuburb(data.suburb || "");
      setProfileCity(data.city || "");
      setProfileProvince(data.province || "");
      setProfilePostalCode(data.postal_code || "");

      const emailResponse = await fetch(`${API_URL}/profile/visit`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const emailData = await emailResponse.json();
      setProfileMessage(
        emailResponse.ok
          ? emailData.message
          : "Profile loaded, but the notification email could not be sent.",
      );
    } catch (err) {
      console.error(err);
      setProfileError("Profile loaded, but the notification email failed.");
    }
  };

  const updateProfile = async (e) => {
    e.preventDefault();
    setProfileMessage("");
    setProfileError("");
    setProfileLoading(true);

    try {
      const response = await fetch(`${API_URL}/profile`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          first_name: profileFirstName,
          last_name: profileLastName,
          email: profileEmail,
          phone: profilePhone,
          address: profileAddress,
          suburb: profileSuburb,
          city: profileCity,
          province: profileProvince,
          postal_code: profilePostalCode,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        setProfileError(data.message || "Failed to update profile.");
        return;
      }

      setUser(data.user);
      setProfileMessage("Profile updated successfully!");
    } catch (err) {
      console.error(err);
      setProfileError("Could not connect to the backend.");
    } finally {
      setProfileLoading(false);
    }
  };

  const updatePassword = async (e) => {
    e.preventDefault();
    setPasswordMessage("");
    setPasswordError("");

    if (profileNewPassword !== profileConfirmPassword) {
      setPasswordError("New passwords do not match.");
      return;
    }

    setPasswordLoading(true);
    try {
      const response = await fetch(`${API_URL}/profile/password`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          current_password: currentPassword,
          new_password: profileNewPassword,
        }),
      });
      const data = await response.json();
      if (!response.ok) {
        setPasswordError(data.message || "Failed to change password.");
        return;
      }
      setCurrentPassword("");
      setProfileNewPassword("");
      setProfileConfirmPassword("");
      setPasswordMessage(data.message);
    } catch (err) {
      console.error(err);
      setPasswordError("Could not connect to the backend.");
    } finally {
      setPasswordLoading(false);
    }
  };

  const loadCustomers = async () => {
    if (!token || user?.role !== "admin") {
      return;
    }

    setCustomersLoading(true);
    setCustomerMessage("");
    setCustomerError("");

    try {
      const response = await fetch(`${API_URL}/admin/customers`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (!response.ok) {
        setCustomerError(data.message || "Failed to load customers.");
        return;
      }

      setCustomers(data.customers || []);
    } catch (err) {
      console.error(err);
      setCustomerError("Could not connect to the backend.");
    } finally {
      setCustomersLoading(false);
    }
  };

  const loadAdminOrders = async () => {
    if (!token || user?.role !== "admin") return;

    setAdminOrdersLoading(true);
    setAdminOrdersError("");
    try {
      const response = await fetch(`${API_URL}/admin/orders`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await readResponse(response);
      if (!response.ok) {
        setAdminOrdersError(data.message || "Failed to load orders.");
        return;
      }
      setAdminOrders(data || []);
    } catch (err) {
      console.error(err);
      setAdminOrdersError("Could not connect to the backend.");
    } finally {
      setAdminOrdersLoading(false);
    }
  };

  const updateAdminOrder = async (orderId, status, estimatedDelivery) => {
    try {
      const response = await fetch(`${API_URL}/admin/orders/${orderId}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          status,
          estimated_delivery: estimatedDelivery || null,
        }),
      });
      const data = await readResponse(response);
      if (!response.ok) {
        showNotification("Update failed", data.message || "Could not update the order.", "error");
        return;
      }
      setAdminOrders((currentOrders) =>
        currentOrders.map((order) =>
          order.id === orderId
            ? { ...order, status: data.status, estimated_delivery: data.estimated_delivery }
            : order,
        ),
      );
      showNotification("Order updated", "The customer can now see the latest delivery status.");
    } catch (err) {
      console.error(err);
      showNotification("Update failed", "Could not connect to the backend.", "error");
    }
  };

  const deleteCustomer = async (customerId) => {
    const confirmed = window.confirm(
      "Are you sure you want to delete this customer account?",
    );

    if (!confirmed) {
      return;
    }

    setCustomerMessage("");
    setCustomerError("");

    try {
      const response = await fetch(
        `${API_URL}/admin/customers/${customerId}`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const data = await response.json();

      if (!response.ok) {
        setCustomerError(data.message || "Failed to delete customer.");
        return;
      }

      setCustomerMessage("Customer account deleted successfully!");
      setCustomers((currentCustomers) =>
        currentCustomers.filter((customer) => customer.id !== customerId),
      );
    } catch (err) {
      console.error(err);
      setCustomerError("Could not connect to the backend.");
    }
  };

  useEffect(() => {
    loadProducts();
  }, []);

  useEffect(() => {
    loadProfile();

    if (token) {
      loadCart();
    }
  }, [token]);

  const handleAuth = async (e) => {
    e.preventDefault();

    setMessage("");

    setError("");

    if (authMode === "register") {
      if (password !== confirmPassword) {
        setError("Passwords do not match.");

        return;
      }

      if (
        !firstName ||
        !lastName ||
        !email ||
        !password ||
        !securityQuestion ||
        !securityAnswer
      ) {
        setError("Please fill in all fields.");

        return;
      }
    }

    try {
      const endpoint =
        authMode === "register" ? `${API_URL}/register` : `${API_URL}/login`;

      const body =
        authMode === "register"
          ? {
              first_name: firstName,

              last_name: lastName,

              email,

              password,

              security_question: securityQuestion,

              security_answer: securityAnswer,
            }
          : {
              email,

              password,
            };

      const response = await fetch(endpoint, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify(body),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.message || "Something went wrong.");

        return;
      }

      if (authMode === "register") {
        setMessage("Registration successful! You can now log in.");

        setFirstName("");

        setLastName("");

        setEmail("");

        setPassword("");

        setConfirmPassword("");

        setSecurityQuestion("");

        setSecurityAnswer("");

        setTimeout(() => {
          setAuthMode("login");

          setMessage("");
        }, 1200);
      } else {
        localStorage.setItem("access_token", data.access_token);

        setToken(data.access_token);

        setUser(data.user);

        setShowAuth(false);

        setEmail("");

        setPassword("");

        setMessage("");

        setError("");
      }
    } catch (err) {
      console.error(err);

      setError("Could not connect to the server.");
    }
  };

  const requestSecurityQuestion = async (e) => {
    e.preventDefault();
    setMessage("");
    setError("");

    try {
      const response = await fetch(`${API_URL}/forgot-password/question`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.message || "Could not find that account.");
        return;
      }

      setForgotUserId(data.user_id);
      setForgotQuestion(data.security_question);
      setForgotStep("answer");
    } catch (err) {
      console.error(err);
      setError("Could not connect to the server.");
    }
  };

  const verifySecurityAnswer = async (e) => {
    e.preventDefault();
    setMessage("");
    setError("");

    try {
      const response = await fetch(`${API_URL}/forgot-password/verify`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: forgotUserId,
          security_answer: forgotAnswer,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.message || "Incorrect answer.");
        return;
      }

      setForgotStep("reset");
    } catch (err) {
      console.error(err);
      setError("Could not connect to the server.");
    }
  };

  const resetPasswordWithSecurityAnswer = async (e) => {
    e.preventDefault();
    setMessage("");
    setError("");

    if (newPassword !== forgotConfirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    try {
      const response = await fetch(`${API_URL}/forgot-password/reset`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: forgotUserId,
          new_password: newPassword,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.message || "Could not reset password.");
        return;
      }

      setMessage(data.message || "Password changed successfully.");
      setTimeout(() => {
        setAuthMode("login");
        setForgotStep("email");
        setForgotUserId(null);
        setForgotQuestion("");
        setForgotAnswer("");
        setNewPassword("");
        setForgotConfirmPassword("");
        setMessage("");
      }, 1200);
    } catch (err) {
      console.error(err);
      setError("Could not connect to the server.");
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("access_token");

    setToken(null);

    setUser(null);

    setCart([]);

    setCartTotal(0);

    setShowCart(false);

    setShowAdmin(false);
  };

  const openCheckout = () => {
    if (!token || user?.role !== "customer") {
      return;
    }

    setCheckoutMessage("");
    setCheckoutError("");
    setShippingFirstName(user.first_name || "");
    setShippingLastName(user.last_name || "");
    setShippingPhone(user.phone || "");
    setShippingAddress(user.address || "");
    setShippingSuburb(user.suburb || "");
    setShippingCity(user.city || "");
    setShippingProvince(user.province || "");
    setShippingPostalCode(user.postal_code || "");
    setCardHolderName("");
    setCardNumber("");
    setCardCvv("");
    setShowCart(false);
    setShowCheckout(true);
  };

  const handleCheckout = async (e) => {
    e.preventDefault();
    setCheckoutMessage("");
    setCheckoutError("");
    setCheckoutLoading(true);

    try {
      const orderResponse = await fetch(`${API_URL}/orders/checkout`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          shipping_first_name: shippingFirstName,
          shipping_last_name: shippingLastName,
          shipping_phone: shippingPhone,
          shipping_address: shippingAddress,
          shipping_suburb: shippingSuburb,
          shipping_city: shippingCity,
          shipping_province: shippingProvince,
          shipping_postal_code: shippingPostalCode,
          payment_account_holder: "Payfast",
          payment_account_number: "Payfast",
        }),
      });

      const orderData = await orderResponse.json();

      if (!orderResponse.ok) {
        setCheckoutError(orderData.message || "Could not create order.");
        return;
      }

      const paymentResponse = await fetch(
        `${API_URL}/payfast/payment/${orderData.order_id}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const paymentData = await paymentResponse.json();

      if (!paymentResponse.ok) {
        setCheckoutError(
          paymentData.message || "Could not start Payfast payment.",
        );
        return;
      }

      const form = document.createElement("form");
      form.method = "POST";
      form.action = paymentData.payment_url;
      form.target = "_self";

      Object.entries(paymentData.payment_data).forEach(([key, value]) => {
        const input = document.createElement("input");
        input.type = "hidden";
        input.name = key;
        input.value = String(value);
        form.appendChild(input);
      });

      document.body.appendChild(form);
      console.log("Sending Payfast payment:", {
        url: form.action,
        fields: Object.keys(paymentData.payment_data),
      });
      form.submit();
    } catch (err) {
      console.error(err);
      setCheckoutError("Could not connect to the server.");
    } finally {
      setCheckoutLoading(false);
    }
  };

  const addToCart = async (productId) => {
    if (!token) {
      setShowAuth(true);

      setAuthMode("login");

      setError("Please log in before adding products to your cart.");

      return;
    }

    if (user?.role !== "customer") {
      setError("Only customers can add items to the cart.");

      return;
    }

    try {
      const response = await fetch(`${API_URL}/cart`, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",

          Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify({
          product_id: productId,

          quantity: 1,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        showNotification("Could not add product", data.message || "Could not add product to cart.", "error");

        return;
      }

      await loadCart();

      showNotification("Product added", "The product has been added to your cart.");
    } catch (err) {
      console.error(err);

      showNotification("Connection failed", "Could not connect to the server.", "error");
    }
  };

  const updateCartQuantity = async (productId, quantity) => {
    if (quantity < 1) {
      return;
    }

    try {
      const response = await fetch(
        `${API_URL}/cart/${productId}`,

        {
          method: "PUT",

          headers: {
            "Content-Type": "application/json",

            Authorization: `Bearer ${token}`,
          },

          body: JSON.stringify({
            quantity,
          }),
        },
      );

      const data = await response.json();

      if (!response.ok) {
        showNotification("Could not update cart", data.message || "Could not update cart.", "error");

        return;
      }

      await loadCart();
    } catch (err) {
      console.error(err);
    }
  };

  const removeFromCart = async (productId) => {
    try {
      const response = await fetch(
        `${API_URL}/cart/${productId}`,

        {
          method: "DELETE",

          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const data = await response.json();

      if (!response.ok) {
        showNotification("Could not remove product", data.message || "Could not remove product.", "error");

        return;
      }

      await loadCart();
    } catch (err) {
      console.error(err);
    }
  };

  const deleteProduct = async (productId) => {
    if (!token) {
      return;
    }

    const confirmed = window.confirm(
      "Are you sure you want to delete this product?",
    );

    if (!confirmed) {
      return;
    }

    try {
      setAdminError("");

      setAdminMessage("");

      const response = await fetch(
        `${API_URL}/products/${productId}`,

        {
          method: "DELETE",

          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const data = await response.json();

      if (!response.ok) {
        setAdminError(data.message || "Could not delete product.");

        return;
      }

      setAdminMessage("Product deleted successfully.");

      if (selectedProduct && selectedProduct.id === productId.toString()) {
        setSelectedProduct(null);
      }

      await loadProducts();
    } catch (err) {
      console.error(err);

      setAdminError("Could not connect to the server.");
    }
  };

  const handleAddProduct = async (e) => {
    e.preventDefault();

    setAdminMessage("");

    setAdminError("");

    if (!productName || !productPrice || !productStock) {
      setAdminError("Name, price and stock are required.");

      return;
    }

    try {
      setAddingProduct(true);

      const formData = new FormData();

      formData.append("name", productName);

      formData.append(
        "description",

        productDescription,
      );

      formData.append("price", productPrice);

      formData.append("category", productCategory);

      formData.append("brand", productBrand);

      formData.append("stock", productStock);

      if (productImage) {
        formData.append("image", productImage);
      }

      const response = await fetch(
        `${API_URL}/products`,

        {
          method: "POST",

          headers: {
            Authorization: `Bearer ${token}`,
          },

          body: formData,
        },
      );

      const data = await response.json();

      if (!response.ok) {
        setAdminError(data.message || "Could not add product.");

        return;
      }

      setAdminMessage("Product added successfully!");

      setProductName("");

      setProductDescription("");

      setProductPrice("");

      setProductCategory("");

      setProductBrand("");

      setProductStock("");

      setProductImage(null);

      const fileInput = document.getElementById("productImage");

      if (fileInput) {
        fileInput.value = "";
      }

      await loadProducts();
    } catch (err) {
      console.error(err);

      setAdminError("Could not connect to the server.");
    } finally {
      setAddingProduct(false);
    }
  };

  const startEditingProduct = (product) => {
    setEditingProduct(product);

    setEditingImage(null);

    setProductName(product.name || "");

    setProductDescription(product.description || "");

    setProductPrice(product.price || "");

    setProductCategory(product.category || "");

    setProductBrand(product.brand || "");

    setProductStock(product.stock ?? "");

    setAdminMessage("");

    setAdminError("");

    window.scrollTo({
      top: 0,

      behavior: "smooth",
    });
  };

  const cancelEditingProduct = () => {
    setEditingProduct(null);

    setEditingImage(null);

    setProductName("");

    setProductDescription("");

    setProductPrice("");

    setProductCategory("");

    setProductBrand("");

    setProductStock("");

    setAdminMessage("");

    setAdminError("");

    const fileInput = document.getElementById("productImage");

    if (fileInput) {
      fileInput.value = "";
    }
  };

  const handleUpdateProduct = async (e) => {
    e.preventDefault();

    if (!editingProduct) {
      return;
    }

    setAdminMessage("");

    setAdminError("");

    if (!productName || productPrice === "" || productStock === "") {
      setAdminError("Name, price and stock are required.");

      return;
    }

    try {
      setUpdatingProduct(true);

      const response = await fetch(
        `${API_URL}/products/${editingProduct.id}`,

        {
          method: "PUT",

          headers: {
            "Content-Type": "application/json",

            Authorization: `Bearer ${token}`,
          },

          body: JSON.stringify({
            name: productName,

            description: productDescription,

            price: productPrice,

            category: productCategory,

            brand: productBrand,

            stock: productStock,
          }),
        },
      );

      const data = await response.json();

      if (!response.ok) {
        setAdminError(data.message || "Could not update product.");

        return;
      }

      if (editingImage) {
        const imageFormData = new FormData();

        imageFormData.append(
          "image",

          editingImage,
        );

        const imageResponse = await fetch(
          `${API_URL}/products/${editingProduct.id}/image`,

          {
            method: "PUT",

            headers: {
              Authorization: `Bearer ${token}`,
            },

            body: imageFormData,
          },
        );

        const imageData = await imageResponse.json();

        if (!imageResponse.ok) {
          setAdminError(
            imageData.message ||
              "Product details updated, but image could not be updated.",
          );

          await loadProducts();

          return;
        }
      }

      setAdminMessage("Product updated successfully!");

      await loadProducts();

      const updatedProduct = await fetch(
        `${API_URL}/products/${editingProduct.id}`,
      );

      if (updatedProduct.ok) {
        const updatedData = await updatedProduct.json();

        setSelectedProduct(updatedData);
      }

      cancelEditingProduct();
    } catch (err) {
      console.error(err);

      setAdminError("Could not connect to the server.");
    } finally {
      setUpdatingProduct(false);
    }
  };

  const formatPrice = (price) => {
    return `R${Number(price).toLocaleString(
      "en-ZA",

      {
        minimumFractionDigits: 2,

        maximumFractionDigits: 2,
      },
    )}`;
  };

  const getProductImage = (product) => {
    if (!product || !product.image) {
      return null;
    }

    return `${API_URL}${product.image}`;
  };

  const categories = [
    ...new Set(products.map((product) => product.category).filter(Boolean)),
  ];

  const brands = [
    ...new Set(products.map((product) => product.brand).filter(Boolean)),
  ];

  const filteredProducts = products
    .filter((product) => {
      const search = searchTerm.toLowerCase();

      return (
        product.name?.toLowerCase().includes(search) ||
        product.brand?.toLowerCase().includes(search) ||
        product.description?.toLowerCase().includes(search)
      );
    })
    .filter((product) => {
      if (selectedCategory === "All") {
        return true;
      }

      return product.category === selectedCategory;
    })
    .filter((product) => {
      if (selectedBrand === "All") {
        return true;
      }

      return product.brand === selectedBrand;
    })
    .sort((a, b) => {
      if (sortOption === "price-low") {
        return Number(a.price) - Number(b.price);
      }

      if (sortOption === "price-high") {
        return Number(b.price) - Number(a.price);
      }

      if (sortOption === "name") {
        return a.name.localeCompare(b.name);
      }

      return 0;
    });

  return (
    <div className="app">
      <Navbar
        user={user}
        cartCount={cart.length}
        onProfile={openProfile}
        onCart={() => {
          loadCart();
          setShowCart(true);
        }}
        onOrders={() => {
          setShowOrders(true);
          loadOrders();
        }}
        onAdmin={() => {
          setShowAdmin(!showAdmin);
          setEditingProduct(null);
        }}
        onLogout={handleLogout}
        onSignUp={() => {
          setAuthMode("register");
          setShowAuth(true);
          setError("");
          setMessage("");
        }}
      />

      {user?.role === "admin" && showAdmin && (
        <section className="admin-section">
          <div className="admin-container">
            <h2>{editingProduct ? "Edit Product" : "Add New Product"}</h2>

            {adminMessage && (
              <div className="success-message">{adminMessage}</div>
            )}

            {adminError && <div className="error-message">{adminError}</div>}

            <form
              onSubmit={editingProduct ? handleUpdateProduct : handleAddProduct}
              className="admin-form"
            >
              <div className="form-group">
                <label>Product Name</label>

                <input
                  type="text"
                  value={productName}
                  onChange={(e) => setProductName(e.target.value)}
                  placeholder="Product name"
                />
              </div>

              <div className="form-group">
                <label>Description</label>

                <textarea
                  value={productDescription}
                  onChange={(e) => setProductDescription(e.target.value)}
                  placeholder="Product description"
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Price</label>

                  <input
                    type="number"
                    step="0.01"
                    value={productPrice}
                    onChange={(e) => setProductPrice(e.target.value)}
                    placeholder="Price"
                  />
                </div>

                <div className="form-group">
                  <label>Stock</label>

                  <input
                    type="number"
                    min="0"
                    value={productStock}
                    onChange={(e) => setProductStock(e.target.value)}
                    placeholder="Stock"
                  />
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Category</label>

                  <input
                    type="text"
                    value={productCategory}
                    onChange={(e) => setProductCategory(e.target.value)}
                    placeholder="Category"
                  />
                </div>

                <div className="form-group">
                  <label>Brand</label>

                  <input
                    type="text"
                    value={productBrand}
                    onChange={(e) => setProductBrand(e.target.value)}
                    placeholder="Brand"
                  />
                </div>
              </div>

              <div className="form-group">
                <label>
                  {editingProduct ? "Replace Product Image" : "Product Image"}
                </label>

                <input
                  id="productImage"
                  type="file"
                  accept="image/*"
                  onChange={(e) => {
                    if (editingProduct) {
                      setEditingImage(e.target.files[0] || null);
                    } else {
                      setProductImage(e.target.files[0] || null);
                    }
                  }}
                />
              </div>

              <div className="admin-buttons">
                <button
                  type="submit"
                  disabled={addingProduct || updatingProduct}
                  className="admin-submit-button"
                >
                  {editingProduct
                    ? updatingProduct
                      ? "Updating..."
                      : "Update Product"
                    : addingProduct
                      ? "Adding..."
                      : "Add Product"}
                </button>

                {editingProduct && (
                  <button
                    type="button"
                    className="admin-cancel-button"
                    onClick={cancelEditingProduct}
                  >
                    Cancel Edit
                  </button>
                )}
              </div>
            </form>

            <div className="admin-products">
              <h3>Manage Products</h3>

              {products.length === 0 ? (
                <p>No products available.</p>
              ) : (
                products.map((product) => (
                  <div className="admin-product-row" key={product.id}>
                    <div>
                      <strong>{product.name}</strong>

                      <p>
                        {formatPrice(product.price)}
                        {" • "}
                        Stock: {product.stock}
                      </p>
                    </div>

                    <div className="admin-product-actions">
                      <button onClick={() => startEditingProduct(product)}>
                        Edit
                      </button>

                      <button onClick={() => deleteProduct(product.id)}>
                        Delete
                      </button>
                    </div>
                  </div>
                ))
              )}
            </div>

            <div className="admin-customer-section">
              <div className="admin-section-header">
                <h3>Customer Profiles</h3>

                <button
                  className="admin-button"
                  onClick={() => {
                    setShowCustomers(true);
                    loadCustomers();
                  }}
                >
                  View Customers
                </button>
              </div>
            </div>

            <div className="admin-orders-section">
              <div className="admin-section-header">
                <div>
                  <span className="section-kicker">Fulfilment</span>
                  <h3>Customer Orders</h3>
                </div>
                <button className="admin-button" onClick={loadAdminOrders}>
                  Refresh Orders
                </button>
              </div>

              {adminOrdersError && <p className="error-message">{adminOrdersError}</p>}
              {adminOrdersLoading ? (
                <p>Loading orders...</p>
              ) : adminOrders.length === 0 ? (
                <p>No customer orders have been placed yet.</p>
              ) : (
                <div className="admin-order-list">
                  {adminOrders.map((order) => (
                    <div className="admin-order-row" key={order.id}>
                      <div>
                        <strong>Order #{order.id}</strong>
                        <p>{order.customer.name} · {order.customer.email}</p>
                        <p>{(order.items || []).map((item) => `${item.product_name} x ${item.quantity}`).join(", ")}</p>
                        <small>Total: {formatPrice(order.total_amount)}</small>
                      </div>
                      <div className="admin-order-controls">
                        <select
                          value={order.status}
                          onChange={(event) => updateAdminOrder(order.id, event.target.value, order.estimated_delivery)}
                        >
                          {[
                            "Processing",
                            "Packed",
                            "Ready for Dispatch",
                            "Shipped",
                            "Out for Delivery",
                            "Delivered",
                            "Cancelled",
                          ].map((status) => <option key={status}>{status}</option>)}
                        </select>
                        <label>
                          Delivery date
                          <input
                            type="date"
                            value={order.estimated_delivery || ""}
                            onChange={(event) => updateAdminOrder(order.id, order.status, event.target.value)}
                          />
                        </label>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </section>
      )}

      {!user && <Hero />}

      {!user && <AboutSection />}

      {!(user?.role === "admin" && showAdmin) && !showProfile && (
        <ProductsSection
          loading={loading}
          products={products}
          filteredProducts={filteredProducts}
          categories={categories}
          brands={brands}
          searchTerm={searchTerm}
          selectedCategory={selectedCategory}
          selectedBrand={selectedBrand}
          sortOption={sortOption}
          onSearchChange={setSearchTerm}
          onCategoryChange={setSelectedCategory}
          onBrandChange={setSelectedBrand}
          onSortChange={setSortOption}
          onClearFilters={() => {
            setSearchTerm("");
            setSelectedCategory("All");
            setSelectedBrand("All");
            setSortOption("default");
          }}
          user={user}
          getProductImage={getProductImage}
          onViewProduct={setSelectedProduct}
          onAddToCart={addToCart}
          formatPrice={formatPrice}
        />
      )}

      {!user && <ContactSection />}

      {showCart && (
        <div className="modal-overlay">
          <div className="modal cart-modal">
            <button className="close-button" onClick={() => setShowCart(false)}>
              ×
            </button>

            <h2>Your Cart</h2>

            {cartLoading ? (
              <p>Loading cart...</p>
            ) : cart.length === 0 ? (
              <p>Your cart is empty.</p>
            ) : (
              <>
                <div className="cart-items">
                  {cart.map((item) => (
                    <div className="cart-item" key={item.product_id}>
                      <div className="cart-item-info">
                        <h3>{item.name}</h3>

                        <p>{formatPrice(item.price)}</p>

                        <p>Subtotal: {formatPrice(item.subtotal)}</p>
                      </div>

                      <div className="cart-item-actions">
                        <button
                          onClick={() =>
                            updateCartQuantity(
                              item.product_id,

                              item.quantity - 1,
                            )
                          }
                          disabled={item.quantity <= 1}
                        >
                          −
                        </button>

                        <span>{item.quantity}</span>

                        <button
                          onClick={() =>
                            updateCartQuantity(
                              item.product_id,

                              item.quantity + 1,
                            )
                          }
                        >
                          +
                        </button>

                        <button
                          className="remove-button"
                          onClick={() => removeFromCart(item.product_id)}
                        >
                          Remove
                        </button>
                      </div>
                    </div>
                  ))}
                </div>

                <div className="cart-total">
                  <strong>Total: {formatPrice(cartTotal)}</strong>
                </div>

                <button
                  className="checkout-button"
                  onClick={openCheckout}
                >
                  Proceed to Checkout
                </button>
              </>
            )}
          </div>
        </div>
      )}

      {showOrders && user?.role === "customer" && (
        <div className="modal-overlay">
          <div className="modal orders-modal">
            <button
              className="close-button"
              onClick={() => setShowOrders(false)}
            >
              ×
            </button>

            <h2>My Orders</h2>

            {ordersError && <div className="error-message">{ordersError}</div>}

            {ordersLoading ? (
              <p>Loading orders...</p>
            ) : orders.length === 0 ? (
              <div className="no-orders">
                <h3>No orders yet</h3>
                <p>Your completed orders will appear here.</p>
              </div>
            ) : (
              <div className="orders-list">
                {orders.map((order) => (
                  <div className="order-card" key={order.id}>
                    <div className="order-header">
                      <div>
                        <h3>Order #{order.id}</h3>
                        <p>
                          {new Date(order.created_at).toLocaleString("en-ZA")}
                        </p>
                      </div>

                      <div className="order-status">
                        <span>{order.status}</span>
                        <small>Payment: {order.payment_status}</small>
                        {order.estimated_delivery && (
                          <small>
                            Delivery: {new Date(`${order.estimated_delivery}T00:00:00`).toLocaleDateString("en-ZA")}
                          </small>
                        )}
                      </div>
                    </div>

                    <div className="order-details">
                      <div>
                        <strong>Purchase Summary</strong>

                        {(order.items || []).map((item, index) => (
                          <p key={`${order.id}-${item.product_name}-${index}`}>
                            {item.product_name} x {item.quantity} |{" "}
                            {formatPrice(item.subtotal)}
                          </p>
                        ))}

                        <p className="order-total">
                          <strong>Total</strong>{" "}
                          {formatPrice(order.total_amount)}
                        </p>
                      </div>

                      <div>
                        <strong>Delivery Address</strong>
                        <p>
                          {order.shipping_address}
                          <br />
                          {order.shipping_suburb}
                          <br />
                          {order.shipping_city}
                          <br />
                          {order.shipping_province}
                          <br />
                          {order.shipping_postal_code}
                        </p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}

      {showCheckout && user?.role === "customer" && (
        <div className="modal-overlay">
          <div className="modal checkout-modal">
            <button
              className="close-button"
              onClick={() => setShowCheckout(false)}
            >
              ×
            </button>

            <h2>Checkout</h2>

            <p className="checkout-subtitle">
              Enter your delivery and payment details.
            </p>

            {checkoutMessage && (
              <div className="success-message">{checkoutMessage}</div>
            )}

            {checkoutError && (
              <div className="error-message">{checkoutError}</div>
            )}

            <form onSubmit={handleCheckout}>
              <h3>Customer Details</h3>

              <div className="form-row">
                <div className="form-group">
                  <label>First Name</label>
                  <input
                    type="text"
                    value={shippingFirstName}
                    onChange={(e) => setShippingFirstName(e.target.value)}
                    required
                  />
                </div>

                <div className="form-group">
                  <label>Last Name</label>
                  <input
                    type="text"
                    value={shippingLastName}
                    onChange={(e) => setShippingLastName(e.target.value)}
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label>Phone Number</label>
                <input
                  type="tel"
                  value={shippingPhone}
                  onChange={(e) => setShippingPhone(e.target.value)}
                  placeholder="0812345678"
                  required
                />
              </div>

              <h3>Delivery Address</h3>

              <div className="form-group">
                <label>Street Address</label>
                <input
                  type="text"
                  value={shippingAddress}
                  onChange={(e) => setShippingAddress(e.target.value)}
                  placeholder="123 Main Road"
                  required
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Suburb</label>
                  <input
                    type="text"
                    value={shippingSuburb}
                    onChange={(e) => setShippingSuburb(e.target.value)}
                    placeholder="Westville"
                    required
                  />
                </div>

                <div className="form-group">
                  <label>City</label>
                  <input
                    type="text"
                    value={shippingCity}
                    onChange={(e) => setShippingCity(e.target.value)}
                    placeholder="Durban"
                    required
                  />
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Province</label>
                  <select
                    value={shippingProvince}
                    onChange={(e) => setShippingProvince(e.target.value)}
                    required
                  >
                    <option value="">Select Province</option>
                    <option value="Eastern Cape">Eastern Cape</option>
                    <option value="Free State">Free State</option>
                    <option value="Gauteng">Gauteng</option>
                    <option value="KwaZulu-Natal">KwaZulu-Natal</option>
                    <option value="Limpopo">Limpopo</option>
                    <option value="Mpumalanga">Mpumalanga</option>
                    <option value="Northern Cape">Northern Cape</option>
                    <option value="North West">North West</option>
                    <option value="Western Cape">Western Cape</option>
                  </select>
                </div>

                <div className="form-group">
                  <label>Postal Code</label>
                  <input
                    type="text"
                    value={shippingPostalCode}
                    onChange={(e) => setShippingPostalCode(e.target.value)}
                    placeholder="3629"
                    required
                  />
                </div>
              </div>

              <h3>Payment Details</h3>

              <div className="form-group">
                <label>Card Holder Name</label>
                <input
                  type="text"
                  value={cardHolderName}
                  onChange={(e) => setCardHolderName(e.target.value)}
                  placeholder="Name on card"
                  required
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Card Number</label>
                  <input
                    type="text"
                    inputMode="numeric"
                    value={cardNumber}
                    onChange={(e) => setCardNumber(e.target.value)}
                    placeholder="0000 0000 0000 0000"
                    required
                  />
                </div>

                <div className="form-group">
                  <label>CVV</label>
                  <input
                    type="text"
                    inputMode="numeric"
                    maxLength="4"
                    value={cardCvv}
                    onChange={(e) => setCardCvv(e.target.value)}
                    placeholder="123"
                    required
                  />
                </div>
              </div>

              <div className="checkout-summary">
                <h3>Order Summary</h3>

                {cart.map((item) => (
                  <div
                    className="checkout-summary-item"
                    key={item.product_id}
                  >
                    <span>
                      {item.name} x {item.quantity}
                    </span>
                    <strong>{formatPrice(item.subtotal)}</strong>
                  </div>
                ))}

                <div className="checkout-total">
                  <span>Total</span>
                  <strong>{formatPrice(cartTotal)}</strong>
                </div>

                <div className="checkout-payment-summary">
                  <strong>Payment Details</strong>
                  <p>Card holder: {cardHolderName || "Not entered"}</p>
                  <p>Card number: {cardNumber || "Not entered"}</p>
                  <p>CVV: {cardCvv || "Not entered"}</p>
                </div>
              </div>

              <button
                type="submit"
                className="checkout-button"
                disabled={checkoutLoading}
              >
                {checkoutLoading ? "Processing..." : "BUY NOW"}
              </button>
            </form>
          </div>
        </div>
      )}

      {showAuth && (
        <div className="modal-overlay">
          <div className="modal auth-modal">
            <button
              className="close-button"
              onClick={() => {
                setShowAuth(false);

                setError("");

                setMessage("");
              }}
            >
              ×
            </button>

            <h2>
              {authMode === "login"
                ? "Login"
                : authMode === "register"
                  ? "Create Account"
                  : "Reset Password"}
            </h2>

            {message && <div className="success-message">{message}</div>}

            {error && <div className="error-message">{error}</div>}

            {authMode === "forgot" ? (
              <form
                onSubmit={
                  forgotStep === "email"
                    ? requestSecurityQuestion
                    : forgotStep === "answer"
                      ? verifySecurityAnswer
                      : resetPasswordWithSecurityAnswer
                }
              >
                {forgotStep === "email" && (
                  <div className="form-group">
                    <label>Email</label>
                    <input
                      type="email"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      placeholder="Email address"
                      required
                    />
                  </div>
                )}

                {forgotStep === "answer" && (
                  <>
                    <p>{forgotQuestion}</p>
                    <div className="form-group">
                      <label>Security Answer</label>
                      <input
                        type="text"
                        value={forgotAnswer}
                        onChange={(e) => setForgotAnswer(e.target.value)}
                        required
                      />
                    </div>
                  </>
                )}

                {forgotStep === "reset" && (
                  <>
                    <div className="form-group">
                      <label>New Password</label>
                      <input
                        type="password"
                        value={newPassword}
                        onChange={(e) => setNewPassword(e.target.value)}
                        required
                      />
                    </div>

                    <div className="form-group">
                      <label>Confirm Password</label>
                      <input
                        type="password"
                        value={forgotConfirmPassword}
                        onChange={(e) =>
                          setForgotConfirmPassword(e.target.value)
                        }
                        required
                      />
                    </div>
                  </>
                )}

                <button type="submit" className="auth-submit-button">
                  {forgotStep === "email"
                    ? "Find Account"
                    : forgotStep === "answer"
                      ? "Verify Answer"
                      : "Change Password"}
                </button>
              </form>
            ) : (
              <form onSubmit={handleAuth}>
                {authMode === "register" && (
                  <>
                    <div className="form-group">
                      <label>First Name</label>
                      <input
                        type="text"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                        placeholder="First name"
                        required
                      />
                    </div>

                    <div className="form-group">
                      <label>Last Name</label>
                      <input
                        type="text"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                        placeholder="Last name"
                        required
                      />
                    </div>
                  </>
                )}

                <div className="form-group">
                  <label>Email</label>
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email address"
                    required
                  />
                </div>

                <div className="form-group">
                  <label>Password</label>
                  <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                  />
                </div>

                {authMode === "register" && (
                  <>
                    <div className="form-group">
                      <label>Confirm Password</label>
                      <input
                        type="password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        placeholder="Confirm password"
                        required
                      />
                    </div>

                    <div className="form-group">
                      <label>Security Question</label>
                      <select
                        value={securityQuestion}
                        onChange={(e) => setSecurityQuestion(e.target.value)}
                        required
                      >
                        <option value="">Select a question</option>
                        <option value="What is your favourite car brand?">
                          What is your favourite car brand?
                        </option>
                        <option value="What was your first pet's name?">
                          What was your first pet&apos;s name?
                        </option>
                        <option value="What city were you born in?">
                          What city were you born in?
                        </option>
                        <option value="What is your dream car?">
                          What is your dream car?
                        </option>
                      </select>
                    </div>

                    <div className="form-group">
                      <label>Security Answer</label>
                      <input
                        type="text"
                        value={securityAnswer}
                        onChange={(e) => setSecurityAnswer(e.target.value)}
                        required
                      />
                    </div>
                  </>
                )}

                <button type="submit" className="auth-submit-button">
                  {authMode === "login" ? "Login" : "Register"}
                </button>
              </form>
            )}

            <div className="auth-switch">
              {authMode === "forgot" ? (
                <p>
                  Remembered your password?{" "}
                  <button
                    onClick={() => {
                      setAuthMode("login");
                      setForgotStep("email");
                      setError("");
                      setMessage("");
                    }}
                  >
                    Login
                  </button>
                </p>
              ) : authMode === "login" ? (
                <p>
                  Don't have an account?{" "}
                  <button
                    onClick={() => {
                      setAuthMode("forgot");
                      setForgotStep("email");

                      setError("");

                      setMessage("");
                    }}
                  >
                    Forgot password?
                  </button>
                  {" "}
                  <button
                    onClick={() => {
                      setAuthMode("register");
                      setError("");
                      setMessage("");
                    }}
                  >
                    Register
                  </button>
                </p>
              ) : (
                <p>
                  Already have an account?{" "}
                  <button
                    onClick={() => {
                      setAuthMode("login");

                      setError("");

                      setMessage("");
                    }}
                  >
                    Login
                  </button>
                </p>
              )}
            </div>
          </div>
        </div>
      )}

      {showCustomers && user?.role === "admin" && (
        <div className="modal-overlay">
          <div className="modal customer-modal">
            <button
              className="close-button"
              onClick={() => setShowCustomers(false)}
            >
              ×
            </button>

            <h2>Customer Profiles</h2>

            {customerMessage && (
              <p className="success-message">{customerMessage}</p>
            )}

            {customerError && (
              <p className="error-message">{customerError}</p>
            )}

            {customersLoading ? (
              <p>Loading customers...</p>
            ) : customers.length === 0 ? (
              <p>No customers have registered yet.</p>
            ) : (
              <div className="customer-list">
                {customers.map((customer) => (
                  <div className="customer-card" key={customer.id}>
                    <div>
                      <h3>{customer.full_name}</h3>

                      <p>
                        <strong>Email:</strong> {customer.email}
                      </p>

                      <p>
                        <strong>Role:</strong> {customer.role}
                      </p>
                    </div>

                    <button
                      className="delete-button"
                      onClick={() => deleteCustomer(customer.id)}
                    >
                      Delete Account
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}

      {showProfile && user?.role === "customer" && (
        <section className="profile-page">
          <div className="profile-page-header">
            <span className="section-kicker">Account</span>
            <h2>My Profile</h2>
            <button className="admin-button" onClick={() => setShowProfile(false)}>
              Back to Products
            </button>
          </div>

            {profileMessage && (
              <p className="success-message">{profileMessage}</p>
            )}

            {profileError && <p className="error-message">{profileError}</p>}

            <form onSubmit={updateProfile}>
              <div className="form-group">
                <label>First Name</label>

                <input
                  type="text"
                  value={profileFirstName}
                  onChange={(e) => setProfileFirstName(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label>Last Name</label>

                <input
                  type="text"
                  value={profileLastName}
                  onChange={(e) => setProfileLastName(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label>Email</label>

                <input
                  type="email"
                  value={profileEmail}
                  onChange={(e) => setProfileEmail(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label>Phone Number</label>
                <input
                  type="tel"
                  value={profilePhone}
                  onChange={(e) => setProfilePhone(e.target.value)}
                />
              </div>

              <h3>Saved Delivery Address</h3>

              <div className="form-group">
                <label>Street Address</label>
                <input
                  type="text"
                  value={profileAddress}
                  onChange={(e) => setProfileAddress(e.target.value)}
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Suburb</label>
                  <input
                    type="text"
                    value={profileSuburb}
                    onChange={(e) => setProfileSuburb(e.target.value)}
                  />
                </div>
                <div className="form-group">
                  <label>City</label>
                  <input
                    type="text"
                    value={profileCity}
                    onChange={(e) => setProfileCity(e.target.value)}
                  />
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Province</label>
                  <select
                    value={profileProvince}
                    onChange={(e) => setProfileProvince(e.target.value)}
                  >
                    <option value="">Select Province</option>
                    <option value="Eastern Cape">Eastern Cape</option>
                    <option value="Free State">Free State</option>
                    <option value="Gauteng">Gauteng</option>
                    <option value="KwaZulu-Natal">KwaZulu-Natal</option>
                    <option value="Limpopo">Limpopo</option>
                    <option value="Mpumalanga">Mpumalanga</option>
                    <option value="Northern Cape">Northern Cape</option>
                    <option value="North West">North West</option>
                    <option value="Western Cape">Western Cape</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Postal Code</label>
                  <input
                    type="text"
                    value={profilePostalCode}
                    onChange={(e) => setProfilePostalCode(e.target.value)}
                  />
                </div>
              </div>

              <button
                type="submit"
                className="admin-button"
                disabled={profileLoading}
              >
                {profileLoading ? "Saving..." : "Save Changes"}
              </button>
            </form>

            <div className="password-section">
              <h3>Change Password</h3>
              {passwordMessage && <p className="success-message">{passwordMessage}</p>}
              {passwordError && <p className="error-message">{passwordError}</p>}
              <form onSubmit={updatePassword}>
                <div className="form-group">
                  <label>Current Password</label>
                  <input
                    type="password"
                    value={currentPassword}
                    onChange={(e) => setCurrentPassword(e.target.value)}
                    required
                  />
                </div>
                <div className="form-row">
                  <div className="form-group">
                    <label>New Password</label>
                    <input
                      type="password"
                      value={profileNewPassword}
                      onChange={(e) => setProfileNewPassword(e.target.value)}
                      minLength="8"
                      required
                    />
                  </div>
                  <div className="form-group">
                    <label>Confirm New Password</label>
                    <input
                      type="password"
                      value={profileConfirmPassword}
                      onChange={(e) => setProfileConfirmPassword(e.target.value)}
                      minLength="8"
                      required
                    />
                  </div>
                </div>
                <button type="submit" className="admin-button" disabled={passwordLoading}>
                  {passwordLoading ? "Changing..." : "Change Password"}
                </button>
              </form>
            </div>
        </section>
      )}

      {selectedProduct && (
        <div className="modal-overlay">
          <div className="modal product-modal">
            <button
              className="close-button"
              onClick={() => setSelectedProduct(null)}
            >
              ×
            </button>

            <div
              className="selected-product-image"
              style={
                getProductImage(selectedProduct)
                  ? {
                      backgroundImage: `url(${getProductImage(
                        selectedProduct,
                      )})`,
                    }
                  : {}
              }
            >
              {!selectedProduct.image && <span>No Image</span>}
            </div>

            <div className="selected-product-info">
              <span>{selectedProduct.brand}</span>

              <h2>{selectedProduct.name}</h2>

              <p>{selectedProduct.description}</p>

              <h3>{formatPrice(selectedProduct.price)}</h3>

              <p>Stock: {selectedProduct.stock}</p>

              {user?.role === "customer" && (
                <button
                  className="cart-button"
                  disabled={selectedProduct.stock <= 0}
                  onClick={() => addToCart(selectedProduct.id)}
                >
                  {selectedProduct.stock > 0 ? "Add to Cart" : "Out of Stock"}
                </button>
              )}
            </div>
          </div>
        </div>
      )}

      <NotificationModal
        notification={notification}
        onClose={() => setNotification(null)}
      />

      <Footer />
    </div>
  );
}

export default App;
