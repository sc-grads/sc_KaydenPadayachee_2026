function ProductCard({
  product,
  imageUrl,
  canAddToCart,
  onView,
  onAddToCart,
  formatPrice,
}) {
  return (
    <article className="product-card">
      <div
        className="product-image"
        style={imageUrl ? { backgroundImage: `url(${imageUrl})` } : {}}
      >
        {!imageUrl && <span>No Image</span>}
      </div>

      <div className="product-info">
        <span className="product-brand">{product.brand}</span>
        <h3>{product.name}</h3>
        <p className="product-description">{product.description}</p>

        <div className="product-bottom">
          <strong className="product-price">
            {formatPrice(product.price)}
          </strong>
          <span className="product-stock">
            {product.stock > 0
              ? `${product.stock} available`
              : "Out of stock"}
          </span>
        </div>

        <div className="product-actions">
          <button className="view-button" onClick={() => onView(product)}>
            View
          </button>

          {canAddToCart && (
            <button
              className="cart-button"
              disabled={product.stock <= 0}
              onClick={() => onAddToCart(product.id)}
            >
              {product.stock > 0 ? "Add to Cart" : "Out of Stock"}
            </button>
          )}
        </div>
      </div>
    </article>
  );
}

export default ProductCard;
