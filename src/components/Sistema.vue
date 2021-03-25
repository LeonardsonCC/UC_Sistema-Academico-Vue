<template>
  <div class="uk-dark">
    <h1 class="uk-padding">Sistema</h1>
    <form>
      <fieldset class="uk-fieldset">
        <legend class="uk-legend">Registro de Notas</legend>
        <div>
          <div class="uk-margin">
            <input
              class="uk-input uk-form-width-large"
              type="text"
              v-model="novoAluno.nome"
              id="nome"
              name="nome"
              placeholder="Nome"
            />
          </div>
          <div class="uk-margin">
            <input
              class="uk-input uk-form-width-large"
              type="number"
              id="nome"
              v-model="novoAluno.notaAtual"
              name="nome"
              placeholder="Nota"
            />
          </div>
          <vk-button type="primary" @click="addNota">Adicionar nota</vk-button>
          <vk-button type="primary" @click="addAluno"
            >Adicionar aluno</vk-button
          >
        </div>
      </fieldset>
    </form>
    <hr />
    <div class="uk-margin-top uk-flex uk-flex-center">
      <table class="uk-table uk-width-1-2">
        <thead>
          <tr>
            <th>Aluno</th>
            <th>Notas</th>
            <th>Média</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(aluno, index) in this.alunos" :key="index">
            <td>{{ aluno.nome }}</td>
            <td>{{ aluno.notas.join(", ") }}</td>
            <td>
              {{
                aluno.notas.reduce(
                  (result, item) => parseInt(item) + result,
                  0
                ) / aluno.notas.length
              }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sistema",
  components: {},
  data: () => {
    return {
      alunos: [],
      novoAluno: {
        nome: "",
        notaAtual: 0,
        notas: [],
      },
    };
  },
  methods: {
    addNota: function() {
      this.novoAluno.notas.push(this.novoAluno.notaAtual);
      this.novoAluno.notaAtual = 0;
    },
    addAluno: function() {
      this.addNota();

      this.alunos.push({ ...this.novoAluno });
      this.novoAluno.nome = "";
      this.novoAluno.notaAtual = 0;
      this.novoAluno.notas = [];
    },
  },
};
</script>

<style></style>
