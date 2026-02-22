import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-category-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './category-list.html',
  styleUrl: './category-list.css'
})
export class CategoryList {
  @Input() categories: string[] = [];
  @Input() activeCategory: string = 'All';
  @Output() categoryChange = new EventEmitter<string>();

  selectCategory(cat: string) {
    this.categoryChange.emit(cat);
  }
}