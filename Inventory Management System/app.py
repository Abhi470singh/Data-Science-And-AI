import streamlit as st
from inventory import Inventory
from product import Product

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Inventory Management System",
    page_icon="📦",
    layout="wide"
)

inventory = Inventory()

st.title("📦 Inventory Management System")
st.write("---")

menu = st.sidebar.selectbox(
    "Select Menu",
    (
        "Home",
        "Add Product",
        "View Products",
        "Search Product",
        "Update Product",
        "Delete Product",
        "Sell Product",
        "Add Stock",
        "Low Stock",
        "Inventory Value"
    )
)

# -------------------- HOME --------------------
if menu == "Home":

    st.header("Dashboard")

    st.metric("Total Products", len(inventory.products))

    total_value = sum(
        p.price * p.quantity
        for p in inventory.products
    )

    st.metric("Inventory Value", f"₹{total_value:,.2f}")

# -------------------- ADD PRODUCT --------------------
elif menu == "Add Product":

    st.header("Add Product")

    product_id = st.number_input("Product ID", step=1)

    name = st.text_input("Product Name")

    price = st.number_input("Price", min_value=0.0)

    quantity = st.number_input("Quantity", step=1, min_value=0)

    if st.button("Add Product"):

        product = Product(
            int(product_id),
            name,
            float(price),
            int(quantity)
        )

        inventory.add_product(product)
        inventory.save_data()

        st.success("Product Added Successfully")

# -------------------- VIEW PRODUCTS --------------------
elif menu == "View Products":

    st.header("All Products")

    if len(inventory.products) == 0:

        st.warning("No Product Available")

    else:

        for p in inventory.products:

            st.write(
                f"**ID:** {p.product_id} | "
                f"**Name:** {p.name} | "
                f"**Price:** ₹{p.price} | "
                f"**Stock:** {p.quantity}"
            )

# -------------------- SEARCH PRODUCT --------------------
elif menu == "Search Product":

    st.header("Search Product")

    pid = st.number_input("Product ID", step=1)

    if st.button("Search"):

        product = inventory.search_product(int(pid))

        if product:

            st.success("Product Found")

            st.write(product)

        else:

            st.error("Product Not Found")

# -------------------- UPDATE PRODUCT --------------------
elif menu == "Update Product":

    st.header("Update Product")

    pid = st.number_input("Product ID", step=1)

    new_name = st.text_input("New Name")

    new_price = st.number_input("New Price", min_value=0.0)

    if st.button("Update"):

        product = inventory.search_product(int(pid))

        if product:

            product.update_product(new_name, new_price)

            inventory.save_data()

            st.success("Updated Successfully")

        else:

            st.error("Product Not Found")

# -------------------- DELETE PRODUCT --------------------
elif menu == "Delete Product":

    st.header("Delete Product")

    pid = st.number_input("Product ID", step=1)

    if st.button("Delete"):

        inventory.delete_product(int(pid))

        inventory.save_data()

        st.success("Deleted Successfully")

# -------------------- SELL PRODUCT --------------------
elif menu == "Sell Product":

    st.header("Sell Product")

    pid = st.number_input("Product ID", step=1)

    qty = st.number_input("Quantity", step=1)

    if st.button("Sell"):

        inventory.sell_product(int(pid), int(qty))

        inventory.save_data()

        st.success("Sale Completed")

# -------------------- ADD STOCK --------------------
elif menu == "Add Stock":

    st.header("Add Stock")

    pid = st.number_input("Product ID", step=1)

    qty = st.number_input("Quantity", step=1)

    if st.button("Add"):

        inventory.add_stock(int(pid), int(qty))

        inventory.save_data()

        st.success("Stock Updated")

# -------------------- LOW STOCK --------------------
elif menu == "Low Stock":

    st.header("Low Stock Products")

    limit = st.number_input(
        "Stock Limit",
        value=5,
        step=1
    )

    found = False

    for p in inventory.products:

        if p.quantity <= limit:

            found = True

            st.error(
                f"{p.name} (ID:{p.product_id}) "
                f"Remaining Stock : {p.quantity}"
            )

    if not found:

        st.success("No Low Stock Product")

# -------------------- INVENTORY VALUE --------------------
elif menu == "Inventory Value":

    st.header("Inventory Value")

    total = sum(
        p.price * p.quantity
        for p in inventory.products
    )

    st.metric(
        "Total Inventory Value",
        f"₹{total:,.2f}"
    )