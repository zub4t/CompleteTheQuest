package com.marcoandbreno.completethequest;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.marcoandbreno.completethequest.common.DailyQuest;

@SpringBootApplication
public class CompleteTheQuestApplication {

	public static void main(String[] args) {
		SpringApplication.run(CompleteTheQuestApplication.class, args);
	}
   @Bean
    public CommandLineRunner commandLineRunner() {
        return args -> {
            // This line will be executed at application startup
            new DailyQuest();
        };
    }
}
