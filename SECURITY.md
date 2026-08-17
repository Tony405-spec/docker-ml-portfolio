# Security Policy

## Supported Scope

This repository contains learning examples for Docker-based machine-learning workflows. Security reports should focus on:

- Dockerfile and container runtime practices.
- Dependency or base-image vulnerabilities.
- Accidental credential exposure in examples or documentation.
- Unsafe workflow guidance that could leak local files or secrets.

## Reporting a Vulnerability

Do not open a public issue containing secrets, exploit details, private URLs, or credentials. Use GitHub private vulnerability reporting when available, or contact the maintainer through an approved private channel.

Please include:

- A short description of the concern.
- The affected file or example.
- Steps to reproduce without exposing secrets.
- Suggested remediation if known.

## Container Safety Guidelines

- Do not bake API keys, passwords, or tokens into Docker images.
- Prefer non-root users for application containers where practical.
- Keep `.env`, credentials, model secrets, and cloud keys out of version control.
- Rebuild images after base-image or dependency security updates.
- Review mounted host directories carefully before running examples with `docker run -v`.
