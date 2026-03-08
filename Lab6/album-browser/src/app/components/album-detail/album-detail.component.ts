import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album.model';
import { ChangeDetectorRef } from '@angular/core';
@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  album: Album | null = null;
  editTitle = '';
  loading = true;
  saving = false;
  saved = false;
  nullInput = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private albumService: AlbumService,
    private cdr: ChangeDetectorRef
  ) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.albumService.getAlbum(id).subscribe({
      next: (data) => {
        this.album = data;
        this.editTitle = data.title;
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: () => { this.loading = false; }
    });
  }

  saveAlbum(): void {
    if (!this.album) return;
    this.saving = true;
    const updated = { ...this.album, title: this.editTitle };
    if(this.editTitle.length > 0){
      this.albumService.updateAlbum(updated).subscribe(() => {
      this.album!.title = this.editTitle;
      this.saving = false;
      this.saved = true;
      this.cdr.detectChanges();
      setTimeout(() => this.saved = false, 2500);
    });
    }else{
      this.saving = false;
      this.nullInput = true;
    }
    
  }

  viewPhotos(): void {
    this.router.navigate(['/albums', this.album!.id, 'photos']);
  }

  goBack(): void {
    this.router.navigate(['/albums']);
  }
}
