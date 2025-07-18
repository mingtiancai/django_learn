<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">Item Management</h1>

    <form @submit.prevent="addItem" class="mb-4">
      <div class="form-row">
        <div class="col">
          <input 
            v-model="newItemName" 
            type="text" 
            class="form-control" 
            placeholder="Item Name" 
            required
          />
        </div>
        <div class="col">
          <input 
            v-model="newItemDescription" 
            type="text" 
            class="form-control" 
            placeholder="Description" 
            required
          />
        </div>
        <div class="col">
          <button type="submit" class="btn btn-primary">Add</button>
        </div>
      </div>
    </form>

    <div class="row">
      <div 
        v-for="item in items" 
        :key="item.id" 
        class="col-md-4 mb-4"
      >
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ item.name }}</h5>
            <p class="card-text">{{ item.description }}</p>
            <button 
              class="btn btn-danger" 
              @click="deleteItem(item.id)"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
      newItemName: '',
      newItemDescription: '',
    };
  },
  created() {
    this.fetchItems();
  },
  methods: {
    async fetchItems() {
      try {
        const response = await axios.get('http://localhost:8000/api/items/');
        this.items = response.data;
      } catch (error) {
        console.error("Error fetching items:", error);
      }
    },
    async addItem() {
      if (this.newItemName && this.newItemDescription) {
        const newItem = {
          name: this.newItemName,
          description: this.newItemDescription,
        };
        try {
          await axios.post('http://localhost:8000/api/items/', newItem);
          this.fetchItems(); // Refresh the item list
          this.newItemName = '';
          this.newItemDescription = '';
        } catch (error) {
          console.error("Error adding item:", error);
        }
      }
    },
    async deleteItem(id) {
      try {
        await axios.delete(`http://localhost:8000/api/items/${id}/`);
        this.fetchItems(); // Refresh the item list
      } catch (error) {
        console.error("Error deleting item:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Add optional custom styles here if needed */
h1 {
  color: #343a40;
}
</style>