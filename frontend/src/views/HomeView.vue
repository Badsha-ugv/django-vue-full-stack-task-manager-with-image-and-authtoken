<template>
  <div>
    <h1 class="text-center">Home Page</h1>
    <div class="row">
      <div class="col-5 mx-auto">
        <div class="card p-3 mx-auto" >
          <input type="text" v-model="title" placeholder="Title "  class="form-control mb-2 "> 
          <textarea name="" v-model="desc" id="" placeholder="Descriptoin" cols="30" rows="6" class="form-control"></textarea>
          <input type="file" name="" @change="imageInput" ref="image" id="">
          <button @click="submitForm" class="mt-2 btn btn-info text-white">Add Task</button>
        </div>
      </div>
    </div>
    <div>
      <div class="row">
        <div class="col-5 mx-auto">
          <div class="card p-3 my-3" v-for="item in items" :key="item.id">
            <h3> <router-link :to="{name:'DetailView',params:{id:item.id}}">{{ item.title }}</router-link></h3>
            <small>{{ item.created_at }}</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'HomeView',
  components: {

  },
  data() {
    return {
      items: [],
      title: '',
      desc: '',
      image:null

    }
  },
  methods: {
    imageInput(e) {
      const f = this.$refs.image.files[0] 
      this.image = f
      console.log('f',f)
    },
    getData(){
      axios.get('/todo/')
        .then(res => {
          this.items = res.data;
          console.log(res.data)

        }).
        catch(err => console.log(err))
    },
    submitForm() {
      
      axios.post('/todo/', {
        title: this.title,
        description: this.desc,
        image: this.image
      },
        {

          headers: {
            'content-type':'multipart/form-data'
          }
        }
      )
      .then(res => {
          this.items.push(res.data);
          this.title = '';
          this.desc = '';
        })
      .catch(err => console.log(err))
    }
  },
  mounted() {
    this.getData() 
  }
}
</script>
