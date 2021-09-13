<template>

    <ul v-if="products && products.length">
      <li class="node-tree" v-for="product in products" :key="product.id">
        {{ product.name }}
        <ProductStateTree :product_states="product.product_states"/>
      </li>
    </ul>

    <ul v-else>
      <li>Нет товаров</li>
    </ul>

</template>

<script>
import backendApi from "@/api/backend-api";
import ProductStateTree from "@/components/ProductStateTree";

export default {
  name: "ProductTree",
  props: {
    category_id: Number
  },
  components: {
    ProductStateTree,
  },
  data() {
    return {
      products: []
    }
  },
  mounted() {
    backendApi
        .get('/api/v1/products/', {params: {category_id: this.category_id}})
        .then(response => {
          this.products = response.data;
        })
  }
}
</script>
