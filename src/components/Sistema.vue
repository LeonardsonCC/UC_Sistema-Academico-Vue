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
              id="nota"
              v-model="notaAtual"
              name="nome"
              placeholder="Nota"
            />
          </div>
          <vk-button id="adicionar" type="primary" @click="addNota">Adicionar nota</vk-button>
          <vk-notification status="danger" :messages.sync="messages"></vk-notification>
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
      notaAtual: 0,
      novoAluno: {
        nome: "",
        notas: [],
      },
      messages:[]
    };
  },
  methods: {
    addNota: function() {
      if(this.notaAtual <= 10 && this.notaAtual >= 0){
        if(this.novoAluno.nome === "" || this.notaAtual === ""){
          this.messages.push("O nome do aluno ou a nota não podem ser vazios!");
        }
        else{
          var aluno = this.alunos.find(obj => obj.nome === this.novoAluno.nome);
          if(aluno){
            aluno.notas.push(this.notaAtual);
            this.notaAtual = 0;
          }
          else{
            this.novoAluno.notas.push(this.notaAtual);
            this.notaAtual = 0;

            this.addAluno();
          }
        }
      }
      else{
         this.messages.push("A nota deve ser de 0 a 10!");
      }
    },
    addAluno: function() {
      this.alunos.push({ ...this.novoAluno });
      this.novoAluno.notas = [];
    },
  },
};
</script>

<style></style>
