  <template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          text
          v-on="on"
        >
          Commands
        </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          {{ group }} - {{ command.name }}
        </v-card-title>

        <v-card-text>
          <div class="text">
            <v-flex left v-for="i in command.command" :key="i.ip">
              <div class="button">
                <v-btn
              @click="toggleButton(i)"
            >
              {{ i.name }}
            </v-btn>
              </div>
          </v-flex>
          </div>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: [ "command", "group" ],
  data() {
      return {
          dialog: false,
          comandos: null,
      }
  },
  methods: {
      toggleButton(comando){
        console.log("Comando é: ", comando)
        console.log('http://' + comando.ip + comando.params)
        axios
        .get('http://' + comando.ip + comando.params)
      }
  }
}
</script>

<style scoped>
.text{
  text-align: center;
}
.button{
  padding-top: 10px;
  padding-bottom: 10px;
}
</style>