<template>
    <div>
        <h3>Update View</h3>

        <div class="row">
      <div class="col-5 mx-auto">
        <div class="card p-3 mx-auto" >
          <input type="text" v-model="todo.title" placeholder="Title "  class="form-control mb-2 "> 
          <textarea name="" v-model="todo.description" id="" placeholder="Descriptoin" cols="30" rows="6" class="form-control"></textarea>
          <input type="file" name="" @change="imageInput" ref="image" id="">
          <button @click="submitForm" class="mt-2 btn btn-info text-white">Add Task</button>
        </div>
      </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios' 

export default {
    name: 'UpdateView',
    data() {
        return {
            todo: {},
            title: '',
            description: "",
            image:null
        }
    },
    methods: {
        imageInput() {
            const f = this.$refs.image.files[0]
            this.image = f
        },
        submitForm() {
            const id = this.$route.params['id']
            const data = {
                title: this.todo.title,
                description: this.todo.description,
                image:this.image
            }
            console.log('submit data',data) 
            axios.put(`/todo/${id}/`, data , {
                headers: {
                    'Content-Type':'multipart/form-data'
                }
            })
                .then(response => { 
                    console.log(response.data)
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                 })
                
        }
    },
    mounted() {
        let id = this.$route.params['id'] 
        axios.get(`/todo/${id}`)
            .then(res => {
            this.todo= res.data 
        })
    }
}
</script>