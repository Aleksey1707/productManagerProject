<template>
  <h1>{{ title }}</h1>
  <div v-if="!categories.length">Загрузка данных</div>
  <div v-else>
    <div class="tree">
      <ul class="tree-list" v-for="category in categories" :key="category.id">
        <CategoryTree :category="category"/>
      </ul>
    </div>
  </div>
</template>

<script>
import CategoryTree from "@/components/CategoryTree"
import backendApi from "@/api/backend-api"

export default {
  name: 'ProductListByCategory',
  components: {
    CategoryTree,
  },
  data() {
    return {
      title: "Список продуктов",
      categories: []
    }
  },
  mounted() {
    backendApi
        .get('/api/v1/categories/')
        .then(response => {
          this.categories = response.data;
        })
  }
}
</script>
