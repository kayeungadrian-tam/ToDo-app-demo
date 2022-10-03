<script setup>
import { ref } from "vue"
import axios from "axios";

const name = ref("");
const title = ref("");
const tasks = ref([]);

const getMethod = async () => {
    const params = { "task_id": title.value }
    const res = await axios.get("http://localhost:8000/tasks", { params: params });

    tasks.value = res.data;

}

const deleteMethod = async () => {
    const res = await axios.delete("http://localhost:8000/tasks");
    console.log(res.response.data)
}

const postMethod = async () => {

    const params = { "title": title.value, "name": name.value };

    const res = await axios.post("http://localhost:8000/tasks", params);
}

</script>
    
<template>
    <h1>API demo: TO-DO App</h1>
    <hr>
    <p>FastApi reference docs: <a href="http://localhost:8000/docs"
            target="_blank"><span>Docs</span></a>

        | <a href="http://localhost:8000/redoc"
            target="_blank"><span>ReDoc</span></a>
    </p>

    <p>Dynamodb Admin: <a href="http://localhost:8001"
            target="_blank"><span>Access</span></a>
    </p>


    <div class="main">
        <div>
            <el-input v-model="title"
                size="large"
                placeholder="Please input" />
        </div>
        <br>
        <div>
            <el-input v-model="name"
                placeholder="Please input" />
        </div>

        <br>
        <div>
            <el-button type="danger"
                @click="deleteMethod">Delete</el-button>

            <el-button type="success"
                @click="postMethod">Post</el-button>

            <el-button type="primary"
                @click="getMethod">Get</el-button>
        </div>
    </div>
    <div style="padding:10px"
        v-for="task in tasks"
        :key="task.name">
        <el-card class="box-card">
            <template #header>
                <div class="card-header">
                    <span>{{task.title}}</span>
                </div>
            </template>
            <p>{{task.name}}</p>
        </el-card>
    </div>
</template>
    
<style scope>
.main {
    padding: 20px;
}

.read-the-docs {
    color: #888;
}
</style>

