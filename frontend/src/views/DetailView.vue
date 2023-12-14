<template>
    <div>
        <div class="row">
            <div class="col-5 mx-auto">
                <h3>Todo Details View</h3>
                <hr>
                <div class="card w-75 p-3 mx-auto">
                   <h4>{{ item.title }}</h4>
                   <span>{{ item.created_at }}</span>
                   <p>{{ item.description }}</p>
                   <img :src="item.image" alt="">
                   <hr>
                   <span>{{ item.done }}</span>
                   <router-link :to="{name:'UpdateView',params:{id:item.id}}" class="btn btn-info btn-sm">Update</router-link>
                   <button class="btn btn-danger btn-sm mt-2" @click="deleteItem">Delete</button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios' 
export default{
    name: 'DetailView',
    data() {
        return {
            item:[]
        }
    },
    methods: {
        getData() {
            const id = this.$route.params['id']
            axios.get(`/todo/${id}`)
                .then(res => {
                    this.item = res.data;
                 console.log(res.data)
                }).catch(error => {
                 console.log(error);
            })
        },
        deleteItem() {
            const id = this.$route.params['id']
            axios.delete(`/todo/${id}`)
               .then(res => {
                    this.$router.push('/')
                 console.log(res.data)
                }).catch(error => {
                 console.log(error);
            })
        }
    },
    mounted() {
        const id = this.$route.params['id']
        console.log('id', id)
        this.getData()
    }
}
</script>
