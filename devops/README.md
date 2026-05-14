# DevOps — interview questions

## Table of contents

- [1. What are CPU-bound and I/O-bound tasks ?](#1-what-are-cpu-bound-and-io-bound-tasks)
- [2. What is the difference between a VM and a container?](#2-what-is-the-difference-between-a-vm-and-a-container)
- [3. Imagine your code works locally, but fails in production. What are some possible reasons, and how would you investigate?](#3-imagine-your-code-works-locally-but-fails-in-production-what-are-some-possible-reasons-and-how-would-you-investigate)
- [4. A bug only happens sometimes in production and you cannot reproduce it locally. What steps would you take to investigate? What extra logging or monitoring would help you without exposing sensitive data?](#4-a-bug-only-happens-sometimes-in-production-and-you-cannot-reproduce-it-locally-what-steps-would-you-take-to-investigate-what-extra-logging-or-monitoring-would-help-you-without-exposing-sensitive-data)

---

#### 1. What are CPU-bound and I/O-bound tasks ?

<details>
<summary>Reveal answer</summary>

The term X-bound designates a type of task which is limited by a specific ressource. It means this task is spending most of its time using that ressource and that its performance depends on the ressource's access.

A CPU-bound task means that this task spends most of its time executing instructions on the CPU - for instance a program computing the decimals of pi. The CPU's performance is the main bottleneck for this task. You improve the performance of a CPU-bound task by using multi-processing.

An I/O-bound task means that this task spends most its time waiting for external operations such as network, database or disk access. In that example, the disk's performance is the main bottleneck for this task. You improve the performance of an I/O-bound task by using concurrency to keep executing operations during the waiting time.

</details>

---

#### 2. What is the difference between a VM and a container?

<details>
<summary>Reveal answer</summary>

In computing, containerization and virtualization both refer to methods for isolating an application to make it operational in multiple environments. Their main differences lie in size and portability.

The differences between containerization and virtualization are:

1. A VM virtualizes the hardware, while containers virtualize the operating system.

2. A virtual machine has its own complete operating system with its own kernel. In contrast, a container does not have its own operating system. It uses the host operating system's kernel.

3. Containers package an application with its dependencies, which makes deployments more consistent and portable across environments.

The trade-off is that VMs provide stronger isolation, while containers are usually more lightweight and portable. Containers are commonly managed at scale with orchestrators such as Kubernetes.

</details>

---

#### 3. Imagine your code works locally, but fails in production. What are some possible reasons, and how would you investigate?

<details>
<summary>Reveal answer</summary>

Possible reasons include different environment variables, dependency versions, interpreter version, database schema, CORS/auth settings, etc.

I would first check the production error message, logs, and stack trace to understand where it fails. Then I would compare local and production environments to identify any differences. If logs are not enough, I would add targeted logs, then try to reproduce locally.

</details>

---

#### 4. A bug only happens sometimes in production and you cannot reproduce it locally. What steps would you take to investigate? What extra logging or monitoring would help you without exposing sensitive data?

<details>
<summary>Reveal answer</summary>

I would start by checking the stack trace and production logs around the failure. Then I would look for patterns: affected users, request payloads, timestamps, specific servers, database records, feature flags, or load spikes. If logs are not enough, I would add targeted logging with correlation/request IDs, but avoid logging secrets or personal data. I would also compare local and production configuration, dependency versions, database schema, environment variables, and external service behavior.

</details>
