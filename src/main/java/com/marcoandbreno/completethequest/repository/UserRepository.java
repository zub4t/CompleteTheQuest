package com.marcoandbreno.completethequest.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.marcoandbreno.completethequest.model.User;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);
}
