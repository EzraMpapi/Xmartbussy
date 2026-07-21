// vite.config.js
import { defineConfig } from "file:///home/project/node_modules/vite/dist/node/index.js";
import react from "file:///home/project/node_modules/@vitejs/plugin-react/dist/index.js";
var vite_config_default = defineConfig({
  plugins: [react()],
  build: {
    outDir: "dist",
    sourcemap: false,
    minify: "esbuild",
    target: "es2020",
    chunkSizeWarningLimit: 4e3,
    rollupOptions: {
      output: {
        manualChunks: {
          "react-vendor": ["react", "react-dom"],
          "charts": ["recharts"],
          "icons": ["lucide-react"],
          "xlsx": ["xlsx"]
        },
        chunkFileNames: "assets/[name]-[hash].js",
        assetFileNames: "assets/[name]-[hash][extname]",
        entryFileNames: "assets/[name]-[hash].js"
      }
    }
  },
  optimizeDeps: {
    include: ["react", "react-dom", "recharts", "lucide-react", "xlsx"]
  },
  server: { port: 5173, host: "0.0.0.0" },
  preview: { port: 4173, host: "0.0.0.0" }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCIvaG9tZS9wcm9qZWN0XCI7Y29uc3QgX192aXRlX2luamVjdGVkX29yaWdpbmFsX2ZpbGVuYW1lID0gXCIvaG9tZS9wcm9qZWN0L3ZpdGUuY29uZmlnLmpzXCI7Y29uc3QgX192aXRlX2luamVjdGVkX29yaWdpbmFsX2ltcG9ydF9tZXRhX3VybCA9IFwiZmlsZTovLy9ob21lL3Byb2plY3Qvdml0ZS5jb25maWcuanNcIjtpbXBvcnQgeyBkZWZpbmVDb25maWcgfSBmcm9tICd2aXRlJ1xuaW1wb3J0IHJlYWN0ICAgICAgICAgICAgZnJvbSAnQHZpdGVqcy9wbHVnaW4tcmVhY3QnXG5cbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZyh7XG4gIHBsdWdpbnM6IFtyZWFjdCgpXSxcblxuICBidWlsZDoge1xuICAgIG91dERpcjogICAgJ2Rpc3QnLFxuICAgIHNvdXJjZW1hcDogZmFsc2UsXG4gICAgbWluaWZ5OiAgICAnZXNidWlsZCcsXG4gICAgdGFyZ2V0OiAgICAnZXMyMDIwJyxcbiAgICBjaHVua1NpemVXYXJuaW5nTGltaXQ6IDQwMDAsXG4gICAgcm9sbHVwT3B0aW9uczoge1xuICAgICAgb3V0cHV0OiB7XG4gICAgICAgIG1hbnVhbENodW5rczoge1xuICAgICAgICAgICdyZWFjdC12ZW5kb3InOiBbJ3JlYWN0JywgJ3JlYWN0LWRvbSddLFxuICAgICAgICAgICdjaGFydHMnOiAgICAgICBbJ3JlY2hhcnRzJ10sXG4gICAgICAgICAgJ2ljb25zJzogICAgICAgIFsnbHVjaWRlLXJlYWN0J10sXG4gICAgICAgICAgJ3hsc3gnOiAgICAgICAgIFsneGxzeCddLFxuICAgICAgICB9LFxuICAgICAgICBjaHVua0ZpbGVOYW1lczogJ2Fzc2V0cy9bbmFtZV0tW2hhc2hdLmpzJyxcbiAgICAgICAgYXNzZXRGaWxlTmFtZXM6ICdhc3NldHMvW25hbWVdLVtoYXNoXVtleHRuYW1lXScsXG4gICAgICAgIGVudHJ5RmlsZU5hbWVzOiAnYXNzZXRzL1tuYW1lXS1baGFzaF0uanMnLFxuICAgICAgfSxcbiAgICB9LFxuICB9LFxuXG4gIG9wdGltaXplRGVwczoge1xuICAgIGluY2x1ZGU6IFsncmVhY3QnLCAncmVhY3QtZG9tJywgJ3JlY2hhcnRzJywgJ2x1Y2lkZS1yZWFjdCcsICd4bHN4J10sXG4gIH0sXG5cbiAgc2VydmVyOiAgeyBwb3J0OiA1MTczLCBob3N0OiAnMC4wLjAuMCcgfSxcbiAgcHJldmlldzogeyBwb3J0OiA0MTczLCBob3N0OiAnMC4wLjAuMCcgfSxcbn0pXG4iXSwKICAibWFwcGluZ3MiOiAiO0FBQXlOLFNBQVMsb0JBQW9CO0FBQ3RQLE9BQU8sV0FBc0I7QUFFN0IsSUFBTyxzQkFBUSxhQUFhO0FBQUEsRUFDMUIsU0FBUyxDQUFDLE1BQU0sQ0FBQztBQUFBLEVBRWpCLE9BQU87QUFBQSxJQUNMLFFBQVc7QUFBQSxJQUNYLFdBQVc7QUFBQSxJQUNYLFFBQVc7QUFBQSxJQUNYLFFBQVc7QUFBQSxJQUNYLHVCQUF1QjtBQUFBLElBQ3ZCLGVBQWU7QUFBQSxNQUNiLFFBQVE7QUFBQSxRQUNOLGNBQWM7QUFBQSxVQUNaLGdCQUFnQixDQUFDLFNBQVMsV0FBVztBQUFBLFVBQ3JDLFVBQWdCLENBQUMsVUFBVTtBQUFBLFVBQzNCLFNBQWdCLENBQUMsY0FBYztBQUFBLFVBQy9CLFFBQWdCLENBQUMsTUFBTTtBQUFBLFFBQ3pCO0FBQUEsUUFDQSxnQkFBZ0I7QUFBQSxRQUNoQixnQkFBZ0I7QUFBQSxRQUNoQixnQkFBZ0I7QUFBQSxNQUNsQjtBQUFBLElBQ0Y7QUFBQSxFQUNGO0FBQUEsRUFFQSxjQUFjO0FBQUEsSUFDWixTQUFTLENBQUMsU0FBUyxhQUFhLFlBQVksZ0JBQWdCLE1BQU07QUFBQSxFQUNwRTtBQUFBLEVBRUEsUUFBUyxFQUFFLE1BQU0sTUFBTSxNQUFNLFVBQVU7QUFBQSxFQUN2QyxTQUFTLEVBQUUsTUFBTSxNQUFNLE1BQU0sVUFBVTtBQUN6QyxDQUFDOyIsCiAgIm5hbWVzIjogW10KfQo=
