# Images Information

## Image Sources

All images used in this website are from **Unsplash** - a free stock photo platform.

### Hero & Header Images

- **Home Hero**: Luxury hotel lobby - https://unsplash.com/photos/hotel-lobby
- **About Header**: Team collaboration - https://unsplash.com/photos/team-meeting
- **Services Header**: Business workspace - https://unsplash.com/photos/workspace
- **Contact Header**: Communication concept - https://unsplash.com/photos/contact

### Service Page Images

#### Hotels
- Header: Modern hotel exterior
- Detail: Luxury hotel room interior

#### Resorts
- Header: Beach resort aerial view
- Detail: Resort pool and amenities

#### Gyms
- Header: Modern gym interior
- Detail: Fitness equipment and training

#### Clubs & Pubs
- Header: Nightclub atmosphere
- Detail: Bar and entertainment venue

#### Wedding Planning
- Header: Wedding ceremony setup
- Detail: Wedding decoration and venue

### About Page Images
- Team collaboration image
- Business strategy image

## Image Optimization

All images are loaded from Unsplash CDN with optimized parameters:
- Width: 800px for detail images
- Width: 1920px for header images
- Format: Auto (WebP when supported)
- Quality: Optimized for web

## Replacing Images

To replace with your own images:

1. **Add images to**: `static/images/`
2. **Update template files**: Replace Unsplash URLs with your image paths
3. **Recommended sizes**:
   - Hero images: 1920x1080px
   - Service detail images: 800x600px
   - Logo: 200x200px (transparent PNG)

### Example:
```html
<!-- Before (Unsplash) -->
<div style="background: url('https://images.unsplash.com/photo-xxx?w=800') center/cover;">

<!-- After (Your image) -->
<div style="background: url('{{ url_for('static', filename='images/your-image.jpg') }}') center/cover;">
```

## Logo

Current logo is a placeholder SVG. Replace with your actual logo:
- Path: `static/images/logo.png`
- Recommended size: 200x200px
- Format: PNG with transparent background
- Or SVG for best quality

## Image Credits

All images from Unsplash are free to use under the Unsplash License:
- Free to use for commercial and non-commercial purposes
- No permission needed
- Attribution appreciated but not required

Learn more: https://unsplash.com/license

## Performance Tips

1. **Compress images** before uploading (use TinyPNG or similar)
2. **Use WebP format** for better compression
3. **Lazy load images** for faster page load
4. **Use CDN** for production deployment
5. **Optimize dimensions** - don't use larger images than needed

## Future Enhancements

- [ ] Add image lazy loading
- [ ] Implement WebP with fallback
- [ ] Add image gallery for services
- [ ] Create custom illustrations
- [ ] Add client logos section
