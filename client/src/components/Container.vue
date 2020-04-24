<template>
  <div class="row">
    <div class="col-lg-6">
      <input type="hidden" v-model="url" class="form-control mt-2" placeholder="Url">
      <input type="text" v-model="title" class="form-control mt-2" placeholder="Title">
      <input type="text" v-model="body" class="form-control mt-2" placeholder="Body">
      <button @click="postBlog" class="btn btn-block btn-dark mt-2">Save</button>
    </div>
    <div class="col-lg-6">
     <table class="table">
        <thead>
          <td>url</td>
          <td>Title</td>
          <td>Body</td>
          <td>Edit</td>
          <td>Delete</td>
        </thead>
        <tbody>
          <tr v-for="blog in blogs" v-bind:key="blog.url">
            <td>{{blog.url}}</td>
            <td>{{blog.title}}</td>
            <td>{{blog.body}}</td>
            <td>
              <button @click="getOne(blog)" class="btn bn-sm btn-success"><i class="fa fa-pencil"></i></button>
            </td>
            <td>
              <button @click="deleteOne(blog.url)" class="btn bn-sm btn-danger"><i class="fa fa-trash"></i></button>
            </td> 
          </tr>
        </tbody>
     </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Container',
  props: {
    msg: String
  },
  data(){
    return{
      blogs:null,
      url:'',
      title:'',
      body:''
    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get(`http://localhost:8000/blogs`)
        .then((res) => {
          this.blogs = res.data;
          this.title = '';
          this.body = '';
          this.url = '';
        })
    },
    getOne(blog){
      this.url = blog.url; 
      this.title = blog.title; 
      this.body = blog.body; 
    },
    deleteOne(url){
      axios.delete(url, { auth: {
        username: 'tissi',
        password: '123123'
      }})
      .then(() => {
        this.getAll();
      })
    },
    postBlog(){
      if (this.url == '') {
        axios.post(`http://localhost:8000/blogs/`, 
          {title: this.title, body: this.body},
          {auth: {username: 'tissi', password: '123123'}}
        )
        .then(() => {
          this.getAll();
        }) 
      } else {
         axios.put(this.url, 
          {title: this.title, body: this.body},
          {auth: {username: 'tissi', password: '123123'}}
        )
        .then(() => {
          this.getAll();
        }) 
      }
      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
