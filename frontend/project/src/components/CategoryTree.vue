<template>
  <li class="node-tree">
    <span class="label">{{ category.name }}</span>

    <ul v-if="category.children && category.children.length">
      <CategoryTree v-for="subcategory in category.children" :category="subcategory" :key="subcategory.id"/>
    </ul>

    <template v-else>
      <ProductTree :category_id="category.id"/>
    </template>

  </li>
</template>

<script>
import ProductTree from "@/components/ProductTree";

export default {
  name: "CategoryTree",
  components: {ProductTree},
  props: {
    category: Object
  },
}
</script>
