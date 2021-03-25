<template>
  <div>
    <h1 class="uk-padding">Sistema Acadêmico bem complexo mesmo</h1>
    <vk-grid class="uk-flex-center uk-flex-middle uk-height-large">
      <form class="uk-width-1-3">
        <fieldset class="uk-fieldset">
          <legend class="uk-legend">Entrar no Sistema</legend>
          <div class="uk-margin">
            <input
              class="uk-input"
              v-model="email"
              type="text"
              placeholder="Login"
            />
          </div>
          <div class="uk-margin">
            <input
              class="uk-input"
              v-model="pass"
              type="password"
              placeholder="Senha"
            />
          </div>
          <vk-button @click="login" type="primary" class="uk-width-1-1"
            >Entrar</vk-button
          >
        </fieldset>
      </form>
    </vk-grid>
  </div>
</template>

<script>
export default {
  name: "Login",
  data: () => {
    return {
      email: "",
      pass: "",
    };
  },
  methods: {
    login: function() {
      if (this.email == "admin" && this.senha == "123")
        this.$router.push("sistema");
    },
  },
};
</script>
