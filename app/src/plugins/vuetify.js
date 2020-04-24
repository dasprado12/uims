import Vue from "vue";
import Vuetify from "vuetify/lib";
import colors from "./colors.js";

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: colors.light.text.primary,
                base: colors.light.base,
                card: colors.light.card,
                background: colors.light.background
            },
            dark: {
                primary: colors.dark.text.primary,
                base: colors.dark.base,
                card: colors.dark.card,
                background: colors.dark.background
            },
        },
    },
});
