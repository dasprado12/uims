<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn
          text
          v-on="on"
        >
            <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
        >
            <v-list-item-title>
              {{ item.title }}
            </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
export default {
    data() {
        return {
            dialog: false,
            items: [
                { title: 'Adicionar Grupo' },
                { title: 'Deletar Grupo' },
            ],
        }
    }
}
</script>