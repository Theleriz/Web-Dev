import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

import { products } from '../data/products';
import { Product } from '../models/product';

import { ProductItem } from '../product-item/product-item';
import { CategoryList } from '../category-list/category-list';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule, ProductItem, CategoryList],
  templateUrl: './product-list.html',
  styleUrl: './product-list.css'
})
export class ProductList {
  products: Product[] = products;
  activeCategory: string = 'All';

  get categories(): string[] {
    return Array.from(new Set(this.products.map(p => p.category)));
  }

  get filteredProducts(): Product[] {
    if (this.activeCategory === 'All') return this.products;
    return this.products.filter(p => p.category === this.activeCategory);
  }

  onCategoryChange(cat: string) {
    this.activeCategory = cat;
  }
}