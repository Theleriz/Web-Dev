export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  rating: number;
  image: string;       // главное фото (можно оставить)
  images: string[];    // минимум 3 фото
  link: string;

  category: string;
  available: boolean;
}