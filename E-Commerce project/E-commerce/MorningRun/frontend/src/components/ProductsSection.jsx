import ProductCard from "./ProductCard";

function ProductsSection({
  loading,
  products,
  filteredProducts,
  categories,
  brands,
  searchTerm,
  selectedCategory,
  selectedBrand,
  sortOption,
  onSearchChange,
  onCategoryChange,
  onBrandChange,
  onSortChange,
  onClearFilters,
  user,
  getProductImage,
  onViewProduct,
  onAddToCart,
  formatPrice,
}) {
  return (
    <section id="products" className="products-section">
      <div className="section-header">
        <h2>Featured Products</h2>
        <p>Browse our automotive collection</p>

        <div className="product-filters">
          <input
            type="text"
            placeholder="Search products..."
            value={searchTerm}
            onChange={(event) => onSearchChange(event.target.value)}
          />

          <select
            value={selectedCategory}
            onChange={(event) => onCategoryChange(event.target.value)}
          >
            <option value="All">All Categories</option>
            {categories.map((category) => (
              <option key={category} value={category}>
                {category}
              </option>
            ))}
          </select>

          <select
            value={selectedBrand}
            onChange={(event) => onBrandChange(event.target.value)}
          >
            <option value="All">All Brands</option>
            {brands.map((brand) => (
              <option key={brand} value={brand}>
                {brand}
              </option>
            ))}
          </select>

          <select
            value={sortOption}
            onChange={(event) => onSortChange(event.target.value)}
          >
            <option value="default">Sort By</option>
            <option value="price-low">Price: Low to High</option>
            <option value="price-high">Price: High to Low</option>
            <option value="name">Name: A-Z</option>
          </select>

          <button className="clear-filter-button" onClick={onClearFilters}>
            Clear
          </button>
        </div>
      </div>

      {loading ? (
        <div className="loading">Loading products...</div>
      ) : products.length === 0 ? (
        <div className="no-products">
          <h3>No products available</h3>
          <p>Admin users can add products through the Admin panel.</p>
        </div>
      ) : (
        <>
          <div className="products-grid">
            {filteredProducts.map((product) => (
              <ProductCard
                key={product.id}
                product={product}
                imageUrl={getProductImage(product)}
                canAddToCart={user?.role === "customer"}
                onView={onViewProduct}
                onAddToCart={onAddToCart}
                formatPrice={formatPrice}
              />
            ))}
          </div>

          {filteredProducts.length === 0 && (
            <p className="no-products">No products found.</p>
          )}
        </>
      )}
    </section>
  );
}

export default ProductsSection;
