// Presentation-only enhancement. The app's API and business logic remain unchanged.
(()=>{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
const update=(target,e)=>{const scene=target.querySelector('.scene3d');if(!scene)return;const r=target.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;scene.style.translate=`${x*12}px ${y*10}px`;};
document.addEventListener('pointermove',e=>{const target=e.target.closest('.hero,.login-art');if(target)update(target,e);});
})();
