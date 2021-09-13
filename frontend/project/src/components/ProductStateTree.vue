<template>

    <ul v-if="product_states && product_states.length">
      <li class="node-tree" v-for="product_state in product_states" :key="product_state.id">
        <strong>Магазин:</strong> {{ product_state.shop.name }}
        <strong>Цена:</strong> {{ product_state.price }} рублей
        <strong>Кол-во:</strong> {{ product_state.quantity }} шт.

      </li>
    </ul>

    <ul v-else>
      <li>Не удалось получить данные о товаре</li>
    </ul>
</template>

<script>
export default {
  name: "ProductStateTree",
  props: {
    product_states: Object
  },
}
</script>
