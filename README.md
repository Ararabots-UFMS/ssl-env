# TO-DO
## all
- Instanciar e configurar todos os containers, sendo eles: ssl-game-controller, grSim, ssl-vision, ssl-gui e ssl-vice.
- Reiniciar os containers, limpar cache e colher logs dos containers.
- Rebuildar/Compilar o código do vice à medida que as atualizações no vice forem feitas.

## Manipular containers
- Criar o container de um processo.
- Run um container de um determinado processo.
- Iniciar um container de determinado processo.
- Parar o container de um determinado processo.
- Reiniciar o container de um determinado processo.
- Excluir container de determinado processo.
- Suspender container de determinado processo.
- Retomar container de determinado processo.
- Enviar sinais ou matar processo dentro de determinado container.
- Bloquear container até o fim de determinado processo.
- CPU shares / quotas / cpuset — limitar CPU (shares, quota, period), fixar CPUs.
- Memory limits / swap / memory reservation — limites e comportamento OOM.
- blkio / IO throttling — limitar I/O de disco.
- pids limit — número máximo de processos permitidos.
- cgroup v2 — comportamento unificado moderno (Kube e runtimes interagem com cgroups para aplicar requests/limits).
bind mounts — montar diretórios do host no container (path host → path container).

volumes gerenciados — volumes nomeados que sobrevivem ao container (drivers: local, NFS, CSI).

tmpfs — filesystem em memória para dados efêmeros.

overlayfs (copy-on-write) — camadas de imagem e escrita no upperdir.

snapshot / image layer caching — builds multi-stage, caching de camadas de imagem.

persistência em orquestradores → PersistentVolume / StorageClass (Kubernetes).

network modes: bridge (default), host, none, macvlan, ipvlan, container:<id> (compartilhar netns), rootless (slirp4netns/pasta).

port forwarding / publish — mapear portas do host para container.

connect / disconnect — ligar containers a redes virtuais ou overlays.

service discovery / DNS — resolução entre containers / serviços (Docker DNS, Kubernetes DNS).

políticas de rede (K8s) e service meshes (Istio/Linkerd) para controle de tráfego e observabilidade em malha.

capabilities — retirar capacidades Linux (CAP_NET_ADMIN, CAP_SYS_ADMIN etc.).

seccomp profiles — filtrar syscalls permitidas (Docker/Podman suportam perfis).

AppArmor / SELinux — LSMs para confinamento de acesso a recursos do kernel/FS.

user namespaces / rootless — executar containers sem root no host (mitiga escapes).

runtime sandboxes — gVisor, Kata Containers, Firecracker — isolamento adicional (mais “VM-like”).

imagem assinada / content trust / scanning — assinatura de imagens, SBOM e varredura de vulnerabilidades (CI).

exec / attach — executar um comando dentro do container ou anexar ao stdio.

logs — coleta de stdout/stderr, drivers de logging (json-file, journald, fluentd, syslog).

inspect — metadados do container (config, mount points, redes, limits).

stats / top — métricas em tempo real de utilização de recursos/processos.

events — stream de eventos do daemon (criação, start, die).

healthchecks / liveness / readiness / startup probes — checagens que permitem reiniciar/retirar tráfego de containers (Kubernetes usa liveness/readiness probes para decidir reinício/serviço).

preStop / postStart hooks (Kubernetes) — passos automatizados ao criar/parar containers.

graceful shutdown — tratar sinais (SIGTERM) e aguardar término antes de SIGKILL.

pull / push / tag / rmi — transferir imagens de/para registries.

dockerfile / buildkit / multi-stage builds — otimizações durante build.

image signing / content trust — verificar proveniência.

layer caching / prune — limpeza e economia de espaço.

scheduling / placement / affinities / anti-affinities / taints & tolerations — onde alocar containers (nós).

replicas / scaling / autoscaling — ajustar réplicas manual/automático.

rolling updates / canary / blue-green — estratégias de deploy sem downtime.

stateful vs stateless — diferença de cuidado com armazenamento e identidade (StatefulSet vs Deployment em K8s).

services / loadbalancers / ingress — exposição e roteamento de tráfego.

logs centralizados (ELK/EFK, Loki), metrics (Prometheus), tracing (OpenTelemetry), audit (auditd/Kubernetes Audit).

profiling/strace/ebpf — investigação de comportamento a nível de syscall/IO.

debug containers / ephemeral containers (K8s) — depurar um pod vivo.

Possíveis funcionalidades:
create(image, cmd, mounts, net, env, resources)

start(container_id) / stop(container_id, timeout) / restart(container_id)

exec(container_id, cmd, tty) / attach(container_id)

inspect(container_id) / logs(container_id, tail, follow) / stats(container_id)

pause(container_id) / unpause(container_id)

commit(container_id, new_image) / export(container_id)

connect_network(container_id, network) / disconnect_network(...)

set_limits(container_id, cpu, memory, pids)

apply_seccomp(container_id, profile.json) / set_capabilities(...)

snapshot_volume(volume) / backup/restore